#!/usr/bin/python3

"""Define a class Square."""

class Square:
    """Represents a square."""

    def __init__(self, size=0):
        """Initializes the square.

        Args:
            size (int, optional): The size of the square.
        Raises:
            TypeError: If size is not a number (float or integer).
            ValueError: If size is less than 0.
        """
        self.size = size

    @property
    def size(self):
        """Getter method to retrieve the size attribute."""
        return (self.__size)

    @size.setter
    def size(self, value):
        """Setter method to set the size attribute.

        Args:
            value (float or int): The new size of the square.
        Raises:
            TypeError: If value is not a number.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, (float, int)):
            raise TypeError("size must be a number")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Computes the area of the square.

        Returns:
            float or int: The area of the square.
        """
        return (self.__size ** 2)

    def __eq__(self, other):
        """Overrides the equality operator."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Overrides the inequality operator."""
        return self.area() != other.area()

    def __lt__(self, other):
        """Overrides the less than operator."""
        return self.area() < other.area()

    def __le__(self, other):
        """Overrides the less than or equal to operator."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Overrides the greater than operator."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Overrides the greater than or equal to operator."""
        return self.area() >= other.area()
