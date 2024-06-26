#!/usr/bin/python3
"""
Module: 4-print_square

This module defines a function `print_square` that prints a square of # characters.

"""


def print_square(size):
    """
    Prints a square of # characters with the given size.

    Parameters:
    size (int): The size length of the square.

    Raises:
    TypeError: If `size` is not an integer or if `size` is a float less than 0.
    ValueError: If `size` is less than 0.

    """
    if not isinstance(size, int):
        if isinstance(size, float) and size >= 0:
            raise TypeError("size must be an integer")
        else:
            raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)

