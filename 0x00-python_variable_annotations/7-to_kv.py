#!/usr/bin/env python3
"""module that implements a function that takes both
str and int or float and returns a tuple"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Returns a tuple containing the string k and the square of
    int/float v.

    Parameters:
        k (str): The string key.
        v (Union[int, float]): The int or float value.

    Returns:
        Tuple[str, float]: A tuple containing the string k and
        the square of v as a float.
    """
    squared_value = float(v) ** 2
    return (k, squared_value)
