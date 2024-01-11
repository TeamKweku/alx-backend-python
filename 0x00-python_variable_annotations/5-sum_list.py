#!/usr/bin/env python3
"""module that implements a typed-annotated sum function"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Returns the sum of a list of floats.

    Parameters:
        input_list (List[float]): The input list of floats.

    Returns:
        float: The sum of the input list.
    """
    return sum(input_list)
