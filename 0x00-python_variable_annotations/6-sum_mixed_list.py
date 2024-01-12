#!/usr/bin/env python3
'''
Defines sum_mixed_list function
'''
from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    '''
    Gets the sum of list of mixed numbers

    Args:
        mxd_lst list[int | float]: the list of numbers

    Return:
        sum of numbers in mxd_lst
    '''
    return sum(mxd_lst)
