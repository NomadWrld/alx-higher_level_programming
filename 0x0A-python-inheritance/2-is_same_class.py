#!/usr/bin/python3

def is_same_class(obj, a_class):
    """
    Check if obj is exactly an instance of the specified class a_class.

    Args:
        obj: Any Python object.
        a_class: The class to compare against.

    Returns:
        True if obj is an instance of a_class, otherwise False.
    """
    return type(obj) is a_class

# Test the implementation
if __name__ == "__main__":
    a = 1
    if is_same_class(a, int):
        print("{} is an instance of the class {}".format(a, int.__name__))
    if is_same_class(a, float):
        print("{} is an instance of the class {}".format(a, float.__name__))
    if is_same_class(a, object):
        print("{} is an instance of the class {}".format(a, object.__name__))
