import asyncio
import logging
import types
import threading

import websockets
import TursomMsg_pb2 as TursomMsg
import TursomSystemMsg_pb2 as TursomSystemMsg
from cacheout import Cache


class ImWebsocketClient:
    def __init__(self, url: str, token: str):
        self.url = url
        self.token = token
        self.ws_handler = ImWebSocketHandler()
        self.prev_handler_map = {}
        self.websocket = None
        self.current_id = None
        self.tasks = []

        @self.handler(TursomMsg.ImMsg.loginResult)
        async def handle_login_result(client, im_msg):
            if im_msg.loginResult.success:
                client.current_id = im_msg.loginResult.imUserId

    def connect_backend(self):
        thread = threading.Thread(target=self.__connect_backend, args=())
        thread.start()
        return thread

    def __connect_backend(self):
        asyncio.run(self.connect())

    async def connect(self):
        websocket = await websockets.connect(self.url)
        self.websocket = websocket

        login_im_msg = TursomMsg.ImMsg()
        login_im_msg.loginRequest.token = self.token
        await websocket.send(login_im_msg.SerializeToString())

        # noinspection PyUnresolvedReferences
        try:
            while not websocket.closed:
                recv = await websocket.recv()
                await self.ws_handler.handle(self, recv)
        except websockets.exceptions.ConnectionClosedOK:
            pass

    def launch(self, task: types.coroutine):
        async def await_task():
            await task
            if await_task in self.tasks:
                self.tasks.remove(await_task)

        await_task = asyncio.create_task(await_task())
        self.tasks.append(await_task)

    def handler(self, msg_type: TursomMsg.ImMsg.DESCRIPTOR):
        return self.ws_handler.handler(msg_type)

    async def wait(self):
        while len(self.tasks) != 0:
            task = self.tasks.pop()
            await task
            if task in self.tasks:
                self.tasks.remove(task)


class ImWebSocketHandler:
    def __init__(self):
        self.handler_map = {}
        self.chatHandlerMap = Cache(maxsize=4096, ttl=60)
        self.broadcastResponseHandlerMap = Cache(maxsize=4096, ttl=60)
        self.broadcastHandlerMap = Cache(maxsize=4096, ttl=60)

        @self.handler(TursomMsg.ImMsg.sendMsgResponse)
        async def handle_send_msg_response(client: ImWebsocketClient, im_msg: TursomMsg.ImMsg):
            req_id = im_msg.sendMsgResponse.reqId
            handler = self.chatHandlerMap.get(req_id)
            if handler is not None:
                await handler(client, im_msg)

        @self.handler(TursomMsg.ImMsg.sendBroadcastRequest)
        async def handle_send_broadcast_response(client: ImWebsocketClient, im_msg: TursomMsg.ImMsg):
            req_id = im_msg.sendBroadcastRequest.reqId
            handler = self.broadcastResponseHandlerMap.get(req_id)
            if handler is not None:
                await handler(client, im_msg)

        @self.handler(TursomMsg.ImMsg.broadcast)
        async def handle_broadcast_msg(client: ImWebsocketClient, im_msg: TursomMsg.ImMsg):
            channel = im_msg.broadcast.channel
            handler = self.broadcastHandlerMap.get(channel)
            if handler is not None:
                await handler(client, im_msg)

        self.handle_send_msg_response = handle_send_msg_response
        self.handle_send_broadcast_response = handle_send_broadcast_response
        self.handle_broadcast_msg = handle_broadcast_msg

    async def handle(self, client: ImWebsocketClient, data: bytes):
        msg = TursomMsg.ImMsg()
        try:
            msg.ParseFromString(data)
        except Exception as e:
            logging.exception(e)
            return
        print(msg)
        content = msg.WhichOneof("content")

        if content in self.handler_map:
            try:
                client.launch(self.handler_map[content](client, msg))
            except Exception as e:
                print(e)
        else:
            print("unsupported msg:", msg)
        pass

    def handler(self, msg_type: TursomMsg.ImMsg.DESCRIPTOR):
        def decorator(func):
            if msg_type in self.handler_map:
                new_func = func
                prev_func = self.handler_map[msg_type]

                async def func_proxy(client: ImWebsocketClient, im_msg: TursomMsg.ImMsg):
                    await prev_func(client, im_msg)
                    await new_func(client, im_msg)

                func = func_proxy
            self.handler_map[msg_type] = func
            return func

        msg_type = msg_type.DESCRIPTOR.name
        return decorator

    def send_chat_msg_handler(self, req_id: str):
        def decorator(func):
            self.chatHandlerMap.set(req_id, func)
            return func

        return decorator

    def send_broadcast_handler(self, req_id: str):
        def decorator(func):
            self.broadcastResponseHandlerMap.set(req_id, func)
            return func

        return decorator

    def recv_broadcast_handler(self, channel: int):
        def decorator(func):
            self.broadcastHandlerMap.set(channel, func)
            return func

        return decorator


class TursomSystemMsgHandler:
    def __init__(self, imWebSocketHandler: ImWebSocketHandler = None):
        self.imWebSocketHandler = imWebSocketHandler # todo
        pass
