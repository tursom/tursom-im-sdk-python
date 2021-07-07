import asyncio
import logging
import threading

import TursomMsg_pb2 as TursomMsg
from ImWebSocketClient import ImWebSocketClient, call_get_live_danmu_record_list


async def sleep(client: ImWebSocketClient):
    print(threading.current_thread())
    record_list = await call_get_live_danmu_record_list(client, "21tsfd1rQ5N", "123")
    print(record_list)
    print("sleep")
    await asyncio.sleep(5)
    print("sleep finish")
    await client.web_socket.close()


# noinspection PyShadowingNames
async def handle_login_result(client: ImWebSocketClient, im_msg: TursomMsg.ImMsg):
    print(client.current_id)
    print("recv login result:", im_msg)

    client.launch(sleep(client))


# noinspection PyShadowingNames
async def handle_on_open(client: ImWebSocketClient):
    client.listen(TursomMsg.ImMsg.loginResult, handle_login_result)


if __name__ == '__main__':
    FORMAT = '%(asctime)s [%(levelname)s] [%(name)s] - %(message)s'
    logging.basicConfig(format=FORMAT)
    client = ImWebSocketClient("ws://127.0.0.1:12345/ws", "CNmX3Zb/m+HAYRILMjF0c2ZkMXJRNU4=")
    # client = ImWebSocketClient("ws://127.0.0.1:12345/ws", "CNeb25i9srXUchILMjFiNjg2YUIzejY=")
    client.handler.logger.setLevel(logging.DEBUG)

    client.on_open(handle_on_open)

    client.connect_backend()
    client.join()
    print("run finish")
