#!/usr/bin/python3

def pow(a, b):
    """
    Computes a to the power of b and returns the value.

    Args:
        a: An integer.
        b: An integer.

    Returns:
        The value of a to the power of b.
    """
    return a ** b

# Test the function
if __name__ == "__main__":
    print(pow(2, 2))
    print(pow(98, 2))
    print(pow(98, 0))
    print(pow(100, -2))
    print(pow(-4, 5))
