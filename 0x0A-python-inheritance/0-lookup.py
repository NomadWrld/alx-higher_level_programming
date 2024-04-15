#!/usr/bin/python3

def lookup(obj):
    """
    Returns the list of available attributes and methods of an object.

    Args:
        obj: Any Python object.

    Returns:
        A list containing the names of attributes and methods of the object.
    """
    return dir(obj)
