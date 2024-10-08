#!/usr/bin/python3
"""
This module contains a function that adds two integers.
"""

def add_integer(a, b=98):
    """
    Adds two integers or floats, casting them to integers if needed.

    Args:
        a: The first number, must be an integer or float.
        b: The second number, must be an integer or float

    Returns:
        The sum of the two numbers as an integer.

    Raises:
        TypeError: If a or b are neither integers nor floats.
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
