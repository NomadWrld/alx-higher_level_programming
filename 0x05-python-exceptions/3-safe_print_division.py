#!/usr/bin/python3
def safe_print_division(a, b):
    """
    Divides two integers and prints the result.

    Args:
        a (int): The dividend.
        b (int): The divisor.

    Returns:
        float or None: The result of the division, or None if division by zero occurs.
    """
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result: {}".format(result))
    return (result)

# Test cases
if __name__ == "__main__":
    a = 12
    b = 2
    result = safe_print_division(a, b)
    print("{:d} / {:d} = {}".format(a, b, result))

    a = 12
    b = 0
    result = safe_print_division(a, b)
    print("{:d} / {:d} = {}".format(a, b, result))
