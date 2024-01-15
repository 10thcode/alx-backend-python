#!/usr/bin/env python3
'''
Defines wait_random function
'''
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    '''
    Waits for a random delay.

    Args:
        max_delay: The maximux delay duration.

    Return:
        The random number
    '''
    rand: float = random.uniform(0, max_delay)
    await asyncio.sleep(rand)
    return rand
