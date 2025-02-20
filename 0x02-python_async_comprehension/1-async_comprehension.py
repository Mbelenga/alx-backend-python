#!/usr/bin/env python3

import asyncio
import random
from typing import List, Generator


async def async_generator() -> Generator[float, None, None]:
    """
    An async generator that yields random numbers between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)


async def async_comprehension() -> List[float]:
    """
    A coroutine that collects 10 random numbers from the async_generator.
    """
    return [number async for number in async_generator()]
