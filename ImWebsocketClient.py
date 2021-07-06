import asyncio
import types

import websockets
import TursomMsg_pb2 as TursomMsg


class ImWebsocketClient:
    def __init__(self, url: str, token: str):
        self.url = url
        self.token = token
        self.handler_map = {}
        self.prev_handler_map = {}
        self.websocket = None
        self.current_id = None
        self.tasks = []

        @self.handler(TursomMsg.ImMsg.loginResult)
        async def _prev_handle_login_result(client, im_msg):
            if im_msg.loginResult.success:
                client.current_id = im_msg.loginResult.imUserId

    async def connect(self):
        loop = asyncio.get_running_loop()
        loop.tasks = self.tasks

        websocket = await websockets.connect(self.url)
        self.websocket = websocket

        login_im_msg = TursomMsg.ImMsg()
        login_im_msg.loginRequest.token = self.token
        await websocket.send(login_im_msg.SerializeToString())

        try:
            while not websocket.closed:
                recv = await websocket.recv()
                recv_im_msg = TursomMsg.ImMsg()
                recv_im_msg.ParseFromString(recv)
                print(recv_im_msg)
                content = recv_im_msg.WhichOneof("content")

                if content in self.handler_map:
                    try:
                        self.launch(self.handler_map[content](self, recv_im_msg))
                    except Exception as e:
                        print(e)
                else:
                    print("unsupported msg:", recv_im_msg)
        except websockets.exceptions.ConnectionClosedOK:
            await self._wait()
            return
        await self._wait()

    def launch(self, task: types.coroutine):
        async def await_task():
            await task
            if await_task in self.tasks:
                self.tasks.remove(await_task)

        await_task = asyncio.create_task(await_task())
        self.tasks.append(await_task)

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

    def _prev_handler(self, msg_type: str):
        def decorator(func):
            self.prev_handler_map[msg_type] = func
            return func

        return decorator

    async def _wait(self):
        while len(self.tasks) != 0:
            task = self.tasks.pop()
            await task
            if task in self.tasks:
                self.tasks.remove(task)
