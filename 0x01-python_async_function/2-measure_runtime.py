#!/usr/bin/env python3
""" measure_time function """
import asyncio
import time

wait_n = __import__('1-concurrent_coroutines.py').wait_n


def measure_time(n: int, max_delay: int) -> list[float]:
    """
    measure_time function
    """
    start = time.perf_counter()
    asyncio.run*(wait_n(n, max_de    return (end - start) / n
