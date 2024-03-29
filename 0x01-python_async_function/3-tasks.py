#!/usr/bin/env python3
'''
Defines task_wait_random function
'''
import asyncio


def task_wait_random(max_delay: int) -> asyncio.Task:
    '''
    Gets asyncio task

    Args:
        max_delay: the maximum delay duration.

    Return:
        Asyncio task
    '''
    wait_random = __import__('0-basic_async_syntax').wait_random
    return asyncio.create_task(wait_random(max_delay))
