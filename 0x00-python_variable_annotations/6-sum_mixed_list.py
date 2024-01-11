#!/usr/bin/env python3
"""module that implements a sum function that takes a mixed list"""
from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Returns the sum of a list of integers and floats.

    Parameters:
        mxd_lst (List[Union[int, float]]): The input list of
        integers and floats.

    Returns:
        float: The sum of the input list.
    """
    return sum(mxd_lst)
