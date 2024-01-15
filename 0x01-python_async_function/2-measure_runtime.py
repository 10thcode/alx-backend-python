#!/usr/bin/env python3
'''
Defines measure_time function
'''
import asyncio
import time


def measure_time(n: int, max_delay: int) -> float:
    '''
    Measures the total excution time for a function.

    Args:
        n: the number of times to execute the function
        max_delay: the max delay durarion

    Return:
        The total execution time.
    '''
    wait_n = __import__('1-concurrent_coroutines').wait_n

    s = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    return (time.perf_counter() - s) / n
