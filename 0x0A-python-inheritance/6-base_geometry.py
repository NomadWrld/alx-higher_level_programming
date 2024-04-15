#!/usr/bin/python3

class BaseGeometry:
    """
    A base geometry class with an unimplemented area() method.
    """

    def area(self):
        """
        Raises:
            Exception: Always raises an Exception with the message "area() is not implemented".
        """
        raise Exception("area() is not implemented")

# Test the implementation
if __name__ == "__main__":
    bg = BaseGeometry()

    try:
        print(bg.area())
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))
