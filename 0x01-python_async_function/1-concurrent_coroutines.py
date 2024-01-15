#!/usr/bin/env python3
'''
Defines wait_n function
'''
import asyncio
from typing import List


async def wait_n(n: int, max_delay: int) -> List[float]:
    '''
    Spawn wait_random n times.

    Args:
        n: the number of times to spawn wait_random function
        max_delay: the max delay duration

    Return:
        list of all the delays
    '''
    wait_random = __import__('0-basic_async_syntax').wait_random
    delays = []

    for i in range(n):
        delays.append(await wait_random(max_delay))

    return sorted(delays)
