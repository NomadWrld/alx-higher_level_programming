#!/usr/bin/python3

def uppercase(s):
    """
    Prints a string in uppercase followed by a new line.

    Args:
        s: The input string.

    Returns:
        None.
    """
    for char in s:
        if ord('a') <= ord(char) <= ord('z'):
            char = chr(ord(char) - 32)
        print(char, end="")
    print()

# Test the function
if __name__ == "__main__":
    uppercase("best")
    uppercase("Best School 98 Battery street")
