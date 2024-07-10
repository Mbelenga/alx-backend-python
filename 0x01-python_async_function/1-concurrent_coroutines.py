#!/usr/bin/env python3
""" multiple coroutine """
import asyncio
import random


from typing import List


wait_random = __import__('0-basic_async_syntax.py').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    function that waits for n random numbers
    """
    coroutines = []
    for _ in range(n):
        coroutines.append(asyncio.create_task(wait_random(max_delay)))
    return sorted(await asyncio.gather(*coroutines))