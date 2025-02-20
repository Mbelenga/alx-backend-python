#!/usr/bin/env python3
"""
Duck Typing annotation
"""
from typing import Mapping, Any, TypeVar, Union


T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """
    Safely retrieve a value from a dictionary
    """
    if key in dct:
        return dct[key]
    else:
        return default
