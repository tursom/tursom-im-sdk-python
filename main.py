import asyncio

import TursomMsg_pb2 as TursomMsg
from ImWebsocketClient import ImWebsocketClient

if __name__ == '__main__':
    client = ImWebsocketClient("ws://127.0.0.1:12345/ws", "CNmX3Zb/m+HAYRILMjF0c2ZkMXJRNU4=")
    # asyncio.run(client.ws_handler.handle(client, "a".encode()))


    @client.handler(TursomMsg.ImMsg.loginResult)
    async def handle_login_result(client: ImWebsocketClient, im_msg: TursomMsg.ImMsg):
        print(client.current_id)
        print("recv login result:", im_msg)

        async def a():
            print("sleep")
            await asyncio.sleep(5)
            print("sleep finish")
            await client.websocket.close()

        client.launch(a())


    asyncio.run(client.connect())
    print("run finish")
