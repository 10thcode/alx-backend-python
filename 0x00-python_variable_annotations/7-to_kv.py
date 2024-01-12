#!/usr/bin/env python3
'''
Defines to_kv function
'''
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''
    Constructs a tuple of mix values

    Args:
        k [str]: a string value
        v [int | float]: an int or float value

    Return:
        [tuple]: tuple containing k and v
    '''
    square = v * v
    return (k, square)
