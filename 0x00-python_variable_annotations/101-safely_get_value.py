#!/usr/bin/env python3
"""a module that implements generic typeso"""
from typing import TypeVar, Any, Optional, Mapping, Union

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> \
                        Union[Any, T]:
    """
    Safely gets a value from a dictionary.

    Parameters:
        dct (Dict[str, T]): The input dictionary.
        key (str): The key to look up in the dictionary.
        default (Optional[T]): The default value to
        return if the key is not present.

    Returns:
        T: The value associated with the key, or
        the default value if the key is not present.
    """
    if key in dct:
        return dct[key]
    else:
        return default
