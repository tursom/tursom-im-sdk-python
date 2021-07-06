import asyncio
import threading

from ImWebsocketClient import ImWebsocketClient
import TursomMsg_pb2 as TursomMsg

client = ImWebsocketClient("ws://127.0.0.1:12345/ws", "CNmX3Zb/m+HAYRILMjF0c2ZkMXJRNU4=")


@client.handler(TursomMsg.ImMsg.loginResult)
async def handle_login_result(client: ImWebsocketClient, im_msg: TursomMsg.ImMsg):
    print(client.current_id)
    print("recv login result:", im_msg)

    async def a():
        print("sleep")
        await asyncio.sleep(5)
        print("sleep finish")

    client.launch(a())
    await client.websocket.close()


if __name__ == '__main__':
    asyncio.run(client.connect())
    print("run finish")

# imMsg = TursomMsg.ImMsg()
# imMsg.msgId = "123"
# print(imMsg.IsInitialized())
# print(imMsg)
# print(imMsg.HasField("content"))
