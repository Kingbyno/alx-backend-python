import asyncio
import random
from typing import Generator

async def async_generator():
    for _ in range(10):
        await asyncio.sleep(1)
        yield ramdom.randint(0, 10)

async def main():
    async for number in async_generator():
        print(number)
if __name__ == "main":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())

