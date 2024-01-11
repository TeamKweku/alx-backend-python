#!/usr/bin/env python3
"""module that retuns a function"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function that multiplies a float by the given
    multiplier.

    Parameters:
        multiplier (float): The multiplier value.

    Returns:
        Callable[[float], float]: A function that takes a float
        and returns its product with the multiplier.
    """
    def multiplier_func(value: float) -> float:
        return value * multiplier

    return multiplier_func
