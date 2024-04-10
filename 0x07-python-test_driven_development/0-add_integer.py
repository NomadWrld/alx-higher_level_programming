#!/usr/bin/python3
"""Defines an integer addition function."""

def add_integer(a, b=98):
    """
    Adds two integers or floats.

    Args:
        a (int or float): First number.
        b (int or float, optional): Second number. Defaults to 98.

    Returns:
        int: Sum of a and b, after converting both to integers.

    Raises:
        TypeError: If a or b is not an integer or float.
    """
    # Check if a is not integer or float
    if (not isinstance(a, (int, float))):
        raise TypeError("a must be an integer")

    # Check if b is not integer or float
    if (not isinstance(b, (int, float))):
        raise TypeError("b must be an integer")

    # Convert a and b to integers
    a = int(a)
    b = int(b)

    # Return the sum of a and b
    return (a + b)
