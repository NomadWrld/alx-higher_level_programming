#!/usr/bin/python3

def is_kind_of_class(obj, a_class):
    """
    Check if obj is an instance of, or if obj is an instance of a class
    that inherited from, the specified class a_class.

    Args:
        obj: Any Python object.
        a_class: The class to check against.

    Returns:
        True if obj is an instance of a_class or its subclass, otherwise False.
    """
    return isinstance(obj, a_class)

# Test the implementation
if __name__ == "__main__":
    a = 1
    if is_kind_of_class(a, int):
        print("{} comes from {}".format(a, int.__name__))
    if is_kind_of_class(a, float):
        print("{} comes from {}".format(a, float.__name__))
    if is_kind_of_class(a, object):
        print("{} comes from {}".format(a, object.__name__))
