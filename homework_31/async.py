import asyncio
import aiohttp


async def async_worker(seconds):
    url = f'http://httpbin.org/delay/{seconds}'
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            result = await response.text()
            return result


async def first_coroutine(seconds):
    print(f"first_coroutine started")
    result = await async_worker(seconds)
    print(f"result first_coroutine: {result}")


async def second_coroutine(seconds):
    print(f"second_coroutine started")
    result = await async_worker(seconds)
    print(f"result second_coroutine: {result}")
    second_future.set_result(12)


async def third_coroutine():
    print(f"third_coroutine started, wait for second_coroutine")
    seconds = await second_future
    result = await async_worker(seconds)
    print(f"result third_coroutine: {result}")
    third_future.set_result(1)


async def fourth_coroutine():
    print(f"fourth_coroutine started, wait for third_coroutine")
    seconds = await third_future
    result = await async_worker(seconds)
    print(f"result fourth_coroutine: {result}")


async def fifth_coroutine(event_loop, seconds):
    print(f"fifth_coroutine started")
    result = await async_worker(seconds)
    print(f"result fifth_coroutine: {result}")
    event_loop.stop()


event_loop = asyncio.get_event_loop()

second_future = asyncio.Future()
third_future = asyncio.Future()

event_loop.create_task(first_coroutine(5))
event_loop.create_task(second_coroutine(20))
event_loop.create_task(third_coroutine())
event_loop.create_task(fourth_coroutine())
event_loop.create_task(fifth_coroutine(event_loop, 30))


event_loop.run_forever()