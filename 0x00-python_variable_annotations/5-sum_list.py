#!/usr/bin/env python3
'''
Defines sum_list function
'''
from typing import List


def sum_list(input_list: List[float]) -> float:
    '''
    Gets the sum of floating numbers in a list

    Args:
        input_list [List[float]]: the list of numbers

    Return:
        sum of numbers in input_list
    '''
    return sum(input_list)
