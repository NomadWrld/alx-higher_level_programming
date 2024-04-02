#!/usr/bin/python3
def raise_exception():
    """
    Raises a type exception.

    Raises:
        TypeError: Always raises a TypeError.
    """
    raise TypeError

# Test case
if __name__ == "__main__":
    try:
        raise_exception()
    except TypeError as te:
        print("Exception raised")
