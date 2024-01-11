#!/usr/bin/env python3
"""this module arguments a function with the correct
    duck-typed annotations
"""
from typing import Sequence, Optional, Any


def safe_first_element(lst: Sequence[Any]) -> Optional[Any]:
    """
    Safely returns the first element of a sequence or None
    if the sequence is empty.

    Parameters:
        lst (typing.Sequence): A sequence of elements.

    Returns:
        Optional[Any]: The first element of the sequence or None
        if the sequence is empty.
    """
    if lst:
        return lst[0]
    else:
        return None
    