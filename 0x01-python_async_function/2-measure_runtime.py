#!/usr/bin/env python3
""" measure_time function """
import asyncio
import time

wait_n = __import__('1-concurrent_coroutines.py').wait_n


async def measure_time(n: int, max_delay: int) -> list[float]:
    """
    measure_time function
    """
    start = time.perf_counter()
    await asyncio.gather(*[wait_n(n, max_delay) for _ in range(n)]
    end=time.perf_counter()
    return (end - start) / n