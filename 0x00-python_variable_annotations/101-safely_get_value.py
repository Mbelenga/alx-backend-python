#!/usr/bin/env python3
""" safely_get_value function """

from typing import TypeVar, Mapping, Any, Union

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                    default: Union[T, None]) -> Union[Any, T]:
        """
        Type Annotations with TypeVar
        """
        if key in dct:
            return dct[key]
        return default
