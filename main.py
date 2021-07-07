import asyncio

import TursomMsg_pb2 as TursomMsg
from ImWebSocketClient import ImWebSocketClient


async def handle_login_result(client: ImWebSocketClient, im_msg: TursomMsg.ImMsg):
    print(client.current_id)
    print("recv login result:", im_msg)

    async def a():
        print("sleep")
        await asyncio.sleep(5)
        print("sleep finish")
        await client.web_socket.close()

    client.launch(a())


if __name__ == '__main__':
    # client = ImWebsocketClient("ws://127.0.0.1:12345/ws", "CNmX3Zb/m+HAYRILMjF0c2ZkMXJRNU4=")
    client = ImWebSocketClient("ws://127.0.0.1:12345/ws", "CNeb25i9srXUchILMjFiNjg2YUIzejY=")

    client.listen(TursomMsg.ImMsg.loginResult, handle_login_result)
    # asyncio.run(client.ws_handler.handle(client, "a".encode()))

    client.connect_backend()
    client.join()
    print("run finish")
