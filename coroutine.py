import asyncio


async def resume_future(future: asyncio.Future):
    await asyncio.sleep(3)
    future.set_result(1)


async def test():
    future = asyncio.Future()
    asyncio.create_task(resume_future(future))
    result = await future
    print(result)


asyncio.run(test())
