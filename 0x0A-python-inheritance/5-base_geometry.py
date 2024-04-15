#!/usr/bin/python3

class BaseGeometry:
    """
    An empty class representing a base geometry.
    """
    pass

# Test the implementation
if __name__ == "__main__":
    bg = BaseGeometry()

    print(bg)            # Output: <__main__.BaseGeometry object at 0x...>
    print(dir(bg))       # Output: List of attributes and methods of bg object
    print(dir(BaseGeometry))  # Output: List of attributes and methods of BaseGeometry class
