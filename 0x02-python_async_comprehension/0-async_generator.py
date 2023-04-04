#!/usr/bin/env python3
""coroutine called async_generator that takes no arguments""

from typing import Generator
import asyncio
import random


async def async_generator() -> Generator[float, None, None]:
    """ Loops 10 times asyncronously, yields random num """

    for i in range(10):
        yield random.random()
        await asyncio.sleep(1)
