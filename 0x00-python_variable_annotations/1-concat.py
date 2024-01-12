#!/usr/bin/env python3
'''
Define concat function
'''


def concat(str1: str, str2: str) -> str:
    '''
    Concatenate two strings

    Args:
        str1 [str]: first string
        str2 [str]: secont string

    Return:
        [str]: Concatenated string of str1 and str2
    '''
    return "{}{}".format(str1, str2)
