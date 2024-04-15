#!/usr/bin/python3

Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """
    Square class that inherits from Rectangle.
    """

    def __init__(self, size):
        """
        Initialize a Square with a given size.

        Args:
            size (int): Size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than or equal to 0.
        """
        super().__init__(size, size)  # Initialize as a rectangle with equal width and height

    def __str__(self):
        """
        Return the string representation of the square.

        Returns:
            str: String representation in the format '[Rectangle] <size>/<size>'.
        """
        return "[Rectangle] {}/{}".format(self.width, self.height)

# Test the implementation
if __name__ == "__main__":
    s = Square(13)

    print(s)        # Output: [Rectangle] 13/13
    print(s.area()) # Output: 169
