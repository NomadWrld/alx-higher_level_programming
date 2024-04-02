#!/usr/bin/python3
import sys

def safe_print_integer_err(value):
    """
    Prints an integer followed by a new line.

    Args:
        value: The value to print.

    Returns:
        bool: True if value has been correctly printed (it means the value is an integer), otherwise False.
    """
    try:
        print("{:d}".format(value))
        return (True)
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return (False)

# Test cases
if __name__ == "__main__":
    value = 89
    has_been_print = safe_print_integer_err(value)
    if not has_been_print:
        print("{} is not an integer".format(value))

    value = -89
    has_been_print = safe_print_integer_err(value)
    if not has_been_print:
        print("{} is not an integer".format(value))

    value = "School"
    has_been_print = safe_print_integer_err(value)
    if not has_been_print:
        print("{} is not an integer".format(value))
