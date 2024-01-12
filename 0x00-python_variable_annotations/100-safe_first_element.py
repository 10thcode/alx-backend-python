#!/usr/bin/env python3
'''
Defines safe_first_element function
'''
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    '''
    Gets the first element of a list

    Args:
        lst: the list

    Return:
        the first element of lst
    '''
    if lst:
        return lst[0]
    else:
        return None
