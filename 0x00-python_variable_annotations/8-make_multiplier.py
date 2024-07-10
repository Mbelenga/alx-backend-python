#!/usr/bin/env python3
""" make_multiplier function """

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    A type-annotated function that takes a float as argument
    and returns a function that multiplies a float
    """
    def multiplier_func(x: float) -> float:
        """ Function that multiplies a float by multiplier """
        return x * multiplier
    return multiplier_func
