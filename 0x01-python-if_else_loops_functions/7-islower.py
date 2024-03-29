#!/usr/bin/python3

def islower(c):
    """
    Checks if a character is lowercase.

    Args:
        c: A character (string of length 1).

    Returns:
        True if c is lowercase, False otherwise.
    """
    if ord('a') <= ord(c) <= ord('z'):
        return True
    else:
        return False

# Test the function
if __name__ == "__main__":
    print("a is {}".format("lower" if islower("a") else "upper"))
    print("H is {}".format("lower" if islower("H") else "upper"))
    print("A is {}".format("lower" if islower("A") else "upper"))
    print("3 is {}".format("lower" if islower("3") else "upper"))
    print("g is {}".format("lower" if islower("g") else "upper"))
