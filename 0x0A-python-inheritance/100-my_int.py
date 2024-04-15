#!/usr/bin/python3

class MyInt(int):
    """
    Custom class MyInt that inherits from int and inverts the behavior of == and != operators.
    """

    def __eq__(self, other):
        """
        Override the equality operator (==) to invert its behavior.

        Args:
            other: The object to compare with.

        Returns:
            bool: True if self is not equal to other, False otherwise.
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Override the inequality operator (!=) to invert its behavior.

        Args:
            other: The object to compare with.

        Returns:
            bool: True if self is equal to other, False otherwise.
        """
        return super().__eq__(other)

# Test the implementation
if __name__ == "__main__":
    my_i = MyInt(3)

    print(my_i)      # Output: 3
    print(my_i == 3) # Output: False
    print(my_i != 3) # Output: True
