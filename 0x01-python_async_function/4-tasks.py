#!/usr/bin/env python3
'''
Defines task_wait_n function
'''
import asyncio
from typing import List


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    '''
    Spawn wait_random n times.

    Args:
        n: the number of times to spawn wait_random function
        max_delay: the max delay duration

    Return:
        list of all the delays
    '''
    task_wait_random = __import__('3-tasks').task_wait_random

    delays = []

    for i in range(n):
        delays.append(await task_wait_random(max_delay))

    return sorted(delays)
