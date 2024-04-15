#!/usr/bin/python3

def inherits_from(obj, a_class):
    """
    Check if obj is an instance of a class that inherited (directly or indirectly)
    from the specified class a_class.

    Args:
        obj: Any Python object.
        a_class: The class to check against.

    Returns:
        True if obj is an instance of a subclass of a_class, otherwise False.
    """
    return isinstance(obj, type) and issubclass(type(obj), a_class)

# Test the implementation
if __name__ == "__main__":
    a = True
    if inherits_from(a, int):
        print("{} inherited from class {}".format(a, int.__name__))
    if inherits_from(a, bool):
        print("{} inherited from class {}".format(a, bool.__name__))
    if inherits_from(a, object):
        print("{} inherited from class {}".format(a, object.__name__))
