#!/usr/bin/env python3
'''
Defines make_multiplier function
'''
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''
    Gets a function that multiplies a float by a multiplier

    Args:
        multiplier [float]: the multiplier

    Return:
        a function
    '''
    def func(n: float) -> float:
        '''
        Multiplies a number by a multiplier

        Args:
            n [float]: the number to be multiplied
        '''
        return n * multiplier

    return func
