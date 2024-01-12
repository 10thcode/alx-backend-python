#!/usr/bin/env python3
'''
Defines element_length function
'''
from typing import Iterable, Sequence, Tuple, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''
    Construct a list of tuples

    Args:
        lst: a list

    Return:
        a list of tuples
    '''
    return [(i, len(i)) for i in lst]
