#!/usr/bin/env python3
"""module that implements a duck type iterable object"""
from typing import Sequence, List, Tuple, Iterable


def element_length(lst: Iterable[Sequence]) -> \
        List[Tuple[Sequence, int]]:
    """
    Returns a list of tuples where each tuple contains an
    element from the input iterable and its corresponding
    length.

    Parameters:
        lst (typing.Iterable[typing.Sequence]): An iterable
        of sequences (e.g., strings, lists, tuples).

    Returns:
        typing.List[typing.Tuple[typing.Sequence, int]]: A
        list of tuples where each tuple contains an element
        from the input iterable and its corresponding length.
    """
    return [(i, len(i)) for i in lst]
