import asyncio
import threading

import TursomMsg_pb2 as TursomMsg
from ImWebSocketClient import ImWebSocketClient


async def sleep():
    print(threading.current_thread())
    print("sleep")
    await asyncio.sleep(5)
    print("sleep finish")
    await client.web_socket.close()


# noinspection PyShadowingNames
async def handle_login_result(client: ImWebSocketClient, im_msg: TursomMsg.ImMsg):
    print(client.current_id)
    print("recv login result:", im_msg)

    client.launch(sleep())


# noinspection PyShadowingNames
async def handle_on_open(client: ImWebSocketClient):
    client.listen(TursomMsg.ImMsg.loginResult, handle_login_result)


if __name__ == '__main__':
    # client = ImWebSocketClient("ws://127.0.0.1:12345/ws", "CNmX3Zb/m+HAYRILMjF0c2ZkMXJRNU4=")
    client = ImWebSocketClient("ws://127.0.0.1:12345/ws", "CNeb25i9srXUchILMjFiNjg2YUIzejY=")

    client.on_open(handle_on_open)

    client.connect_backend()
    client.join()
    print("run finish")
