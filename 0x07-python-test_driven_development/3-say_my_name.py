#!/usr/bin/python3
"""
Module: 3-say_my_name

This module defines a function `say_my_name` that prints a formatted name string.

"""


def say_my_name(first_name, last_name=""):
    """
    Prints a formatted name string.

    Parameters:
    first_name (str): The first name.
    last_name (str, optional): The last name. Defaults to an empty string.

    Raises:
    TypeError: If `first_name` or `last_name` is not a string.

    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    full_name = f"My name is {first_name} {last_name}" if last_name else f"My name is {first_name}"
    print(full_name)
