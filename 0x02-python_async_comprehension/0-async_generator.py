#!/usr/bin/env python3

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    An async generator that yields random numbers between 0 and 1.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
