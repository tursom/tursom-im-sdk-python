import asyncio
import logging
import threading
import types
from typing import Callable, Coroutine, Optional

import websockets
from cacheout import Cache
from google.protobuf.any_pb2 import Any

import TursomMsg_pb2 as TursomMsg
import TursomSystemMsg_pb2 as TursomSystemMsg

__ImWebSocketClientNumber = 0


class ImWebSocketClient:
    def __init__(self, url: str, token: str):
        self.url = url
        self.token = token
        self.handler = ImWebSocketHandler()
        self.lock = threading.RLock()
        self.web_socket = None
        self.current_id = None
        self.tasks = []
        self.thread = None
        self.on_open_handler = None
        self.on_close_handler = None

        @self.listen(TursomMsg.ImMsg.loginResult)
        async def handle_login_result(client, im_msg):
            if im_msg.loginResult.success:
                client.current_id = im_msg.loginResult.imUserId

    def connect_backend(self) -> Optional[threading.Thread]:
        with self.lock:
            if self.thread is not None:
                return
            global __ImWebSocketClientNumber
            __ImWebSocketClientNumber += 1
            self.thread = threading.Thread(
                name=f"ImWebSocketClient-{__ImWebSocketClientNumber}", daemon=True,
                target=self.__connect_backend, args=())
        self.thread.start()
        return self.thread

    def __connect_backend(self):
        asyncio.run(self.connect())

    async def connect(self):
        with self.lock:
            if self.web_socket is not None:
                return
            self.thread = threading.current_thread()
            web_socket = await websockets.connect(self.url)
            self.web_socket = web_socket

        login_im_msg = TursomMsg.ImMsg()
        login_im_msg.loginRequest.token = self.token
        await web_socket.send(login_im_msg.SerializeToString())

        with self.lock:
            if self.on_open_handler is not None:
                await self.on_open_handler(self)

        # noinspection PyUnresolvedReferences
        try:
            while not web_socket.closed:
                recv = await web_socket.recv()
                await self.handler.handle(self, recv)
        except websockets.exceptions.ConnectionClosedOK:
            pass

        with self.lock:
            if self.on_close_handler is not None:
                await self.on_close_handler(self)

    def launch(self, task: types.coroutine):
        current_thread = threading.current_thread()
        if current_thread != self.thread:
            raise RuntimeWarning(f"invalid thread {current_thread}")

        async def await_task():
            await task
            if await_task in self.tasks:
                self.tasks.remove(await_task)

        await_task = asyncio.create_task(await_task())
        self.tasks.append(await_task)

    def listen(
            self, msg_type: TursomMsg.ImMsg.DESCRIPTOR,
            handler=None
    ):
        return self.handler.listen(msg_type, handler)

    # noinspection DuplicatedCode
    def on_open(
            self,
            handler=None
    ):
        def decorator(func: Callable[[ImWebSocketClient], Coroutine[None, None, None]]):
            prev_func = self.on_open_handler
            with self.lock:
                if prev_func is not None:
                    async def func_proxy(client: ImWebSocketClient):
                        await prev_func(client)
                        await func(client)

                    self.on_open_handler = func_proxy
                else:
                    self.on_open_handler = func
            return func

        if handler is None:
            return decorator
        else:
            return decorator(handler)

    # noinspection DuplicatedCode
    def on_close(
            self,
            handler=None
    ):
        def decorator(func: Callable[[ImWebSocketClient], Coroutine[None, None, None]]):
            prev_func = self.on_close_handler

            with self.lock:
                if prev_func is not None:
                    async def func_proxy(client: ImWebSocketClient):
                        await prev_func(client)
                        await func(client)

                    self.on_close_handler = func_proxy
                else:
                    self.on_close_handler = func
            return func

        if handler is None:
            return decorator
        else:
            return decorator(handler)

    async def wait(self):
        while len(self.tasks) != 0:
            task = self.tasks.pop()
            await task
            if task in self.tasks:
                self.tasks.remove(task)

    def join(self, timeout: float = None):
        if self.thread is not None:
            self.thread.join(timeout)


class ImWebSocketHandler:
    def __init__(self):
        self.handler_map_lock = threading.RLock()
        self.handler_map = {}
        self.chatHandlerMap = Cache(maxsize=0, ttl=60)
        self.broadcastResponseHandlerMap = Cache(maxsize=0, ttl=60)
        self.broadcastHandlerMap = Cache(maxsize=0, ttl=60)
        self.system = TursomSystemMsgHandler(self)
        self.broadcast = TursomSystemMsgHandler()

        @self.listen(TursomMsg.ImMsg.sendMsgResponse)
        async def handle_send_msg_response(client: ImWebSocketClient, im_msg: TursomMsg.ImMsg):
            req_id = im_msg.sendMsgResponse.reqId
            handler = self.chatHandlerMap.get(req_id)
            if handler is not None:
                await handler(client, im_msg)

        @self.listen(TursomMsg.ImMsg.sendBroadcastRequest)
        async def handle_send_broadcast_response(client: ImWebSocketClient, im_msg: TursomMsg.ImMsg):
            req_id = im_msg.sendBroadcastRequest.reqId
            handler = self.broadcastResponseHandlerMap.get(req_id)
            if handler is not None:
                await handler(client, im_msg)

        @self.listen(TursomMsg.ImMsg.broadcast)
        async def handle_broadcast_msg(client: ImWebSocketClient, im_msg: TursomMsg.ImMsg):
            channel = im_msg.broadcast.channel
            handler = self.broadcastHandlerMap.get(channel)
            if handler is not None:
                await handler(client, im_msg)

        self.handle_send_msg_response = handle_send_msg_response
        self.handle_send_broadcast_response = handle_send_broadcast_response
        self.handle_broadcast_msg = handle_broadcast_msg

    async def handle(self, client: ImWebSocketClient, data: bytes):
        msg = TursomMsg.ImMsg()
        try:
            msg.ParseFromString(data)
        except Exception as e:
            logging.exception(e)
            return
        print(msg)
        content = msg.WhichOneof("content")
        with self.handler_map_lock:
            if content in self.handler_map:
                try:
                    client.launch(self.handler_map[content](client, msg))
                except Exception as e:
                    logging.exception(e)
            else:
                print("unsupported msg:", msg)

    def listen(
            self, msg_type: TursomMsg.ImMsg.DESCRIPTOR,
            handler: Optional[Callable[[ImWebSocketClient, TursomMsg.ImMsg],
                                       Coroutine[None, None, None]]] = None
    ):
        def decorator(func: Callable[[ImWebSocketClient, TursomMsg.ImMsg],
                                     Coroutine[None, None, None]]):
            with self.handler_map_lock:
                if msg_type in self.handler_map:
                    new_func = func
                    prev_func = self.handler_map[msg_type]

                    async def func_proxy(client: ImWebSocketClient, im_msg: TursomMsg.ImMsg):
                        await prev_func(client, im_msg)
                        await new_func(client, im_msg)

                    self.handler_map[msg_type] = func_proxy
                else:
                    self.handler_map[msg_type] = func

            return func

        msg_type = msg_type.DESCRIPTOR.name
        if handler is None:
            return decorator
        else:
            return decorator(handler)

    def send_chat_msg_handler(
            self, req_id: str,
            handler: Optional[Callable[[ImWebSocketClient, TursomMsg.ImMsg],
                                       Coroutine[None, None, None]]] = None
    ):
        def decorator(func):
            self.chatHandlerMap.set(req_id, func)
            return func

        if handler is None:
            return decorator
        else:
            return decorator(handler)

    def send_broadcast_handler(
            self, req_id: str,
            handler: Optional[Callable[[ImWebSocketClient, TursomMsg.ImMsg],
                                       Coroutine[None, None, None]]] = None
    ):
        def decorator(func):
            self.broadcastResponseHandlerMap.set(req_id, func)
            return func

        if handler is None:
            return decorator
        else:
            return decorator(handler)

    def recv_broadcast_handler(
            self, channel: int,
            handler: Optional[Callable[[ImWebSocketClient, TursomMsg.ImMsg],
                                       Coroutine[None, None, None]]] = None
    ):
        def decorator(func):
            self.broadcastHandlerMap.set(channel, func)
            return func

        if handler is None:
            return decorator
        else:
            return decorator(handler)


class TursomSystemMsgHandler:
    def __init__(self, im_web_socket_handler: ImWebSocketHandler = None):
        self.imWebSocketHandler = im_web_socket_handler
        self.handlerMapLock = threading.RLock()
        self.handlerMap = {}
        self.msgContextHandlerMap = Cache(maxsize=0, ttl=60)
        self.liveDanmuRecordListHandlerMap = Cache(maxsize=0, ttl=60)
        self.liveDanmuRecordHandlerMap = Cache(maxsize=0, ttl=60)

        if im_web_socket_handler is not None:
            self.register_to_im_web_socket_handler(im_web_socket_handler)

        # noinspection PyPep8Naming
        @self.register_handler(TursomSystemMsg.ReturnLiveDanmuRecordList)
        async def ReturnLiveDanmuRecordListHandler(client, receiveMsg, listenLiveRoom):
            handler = self.liveDanmuRecordListHandlerMap.get(listenLiveRoom.reqId)
            if handler is not None:
                await handler(client, receiveMsg, listenLiveRoom)

        # noinspection PyPep8Naming
        @self.register_handler(TursomSystemMsg.ReturnLiveDanmuRecord)
        async def ReturnLiveDanmuRecordHandler(client, receiveMsg, listenLiveRoom):
            handler = self.liveDanmuRecordHandlerMap.get(listenLiveRoom.reqId)
            if handler is not None:
                await handler(client, receiveMsg, listenLiveRoom)

    def register_to_im_web_socket_handler(self, im_web_socket_handler: ImWebSocketHandler):
        im_web_socket_handler.listen(TursomMsg.ImMsg.chatMsg, self.handle)
        im_web_socket_handler.system = self

    async def default(self, client: ImWebSocketClient, im_msg: TursomMsg.ImMsg):
        handler = self.msgContextHandlerMap.get(im_msg.broadcast.content.WhichOneof("content"))
        if handler is not None:
            await handler(client, im_msg)

    async def handle(self, client: ImWebSocketClient, im_msg: TursomMsg.ImMsg):
        # noinspection SpellCheckingInspection
        if im_msg.WhichOneof("content") != "CHATMSG" or im_msg.chatMsgcontent.WhichOneof("content") != "EXT":
            return await self.default(client, im_msg)
        ext = im_msg.chatMsg.content.ext
        await self.handle_ext(client, im_msg, ext)

    async def handle_broadcast(self, client: ImWebSocketClient, im_msg: TursomMsg.ImMsg):
        # noinspection SpellCheckingInspection
        if im_msg.WhichOneof("content") != "BROADCAST" or im_msg.broadcast.content.WhichOneof("content") != "EXT":
            return await self.default(client, im_msg)
        ext = im_msg.chatMsg.content.ext
        await self.handle_ext(client, im_msg, ext)

    async def handle_ext(self, client: ImWebSocketClient, im_msg: TursomMsg.ImMsg, ext: Any):
        with self.handlerMapLock:
            for msg_type, handler in self.handlerMap.items():
                if ext.Is(msg_type):
                    msg = msg_type()
                    ext.Unpack(msg)
                    await handler(client, im_msg, msg)
                    return

    # noinspection PyUnresolvedReferences
    def register_handler(
            self, handle_type,
            handler: Optional[Callable[[ImWebSocketClient, TursomMsg.ImMsg],
                                       Coroutine[None, None, None]]] = None
    ):
        def decorator(func):
            with self.handlerMapLock:
                self.handlerMap[handle_type] = func
            return func

        if handler is None:
            return decorator
        else:
            return decorator(handler)

    # noinspection PyPep8Naming
    def addLiveDanmuRecordListHandler(
            self, reqId: str,
            handler: Optional[Callable[[ImWebSocketClient, TursomMsg.ImMsg],
                                       Coroutine[None, None, None]]] = None
    ):
        def decorator(func):
            self.liveDanmuRecordListHandlerMap.add(reqId, func)
            return func

        if handler is None:
            return decorator
        else:
            return decorator(handler)

    # noinspection PyPep8Naming
    def addLiveDanmuRecordHandler(
            self, reqId: str,
            handler: Optional[Callable[[ImWebSocketClient, TursomMsg.ImMsg],
                                       Coroutine[None, None, None]]] = None
    ):
        def decorator(func):
            self.liveDanmuRecordHandlerMap.add(reqId, func)
            return func

        if handler is None:
            return decorator
        else:
            return decorator(handler)
