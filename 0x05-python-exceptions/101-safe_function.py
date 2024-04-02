#!/usr/bin/python3
import sys

def safe_function(fct, *args):
    """
    Executes a function safely.

    Args:
        fct: The function to execute.
        *args: Arguments to pass to the function.

    Returns:
        Any: The result of the function, or None if an exception occurs.
    """
    try:
        result = fct(*args)
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return None
    else:
        return result

# Example functions
def divide(a, b):
    return a / b

def print_list(my_list, length):
    for i in range(length):
        print(my_list[i])
    return length

# Test cases
if __name__ == "__main__":
    result = safe_function(divide, 10, 2)
    print("Result of divide: {}".format(result))

    result = safe_function(divide, 10, 0)
    print("Result of divide: {}".format(result))

    result = safe_function(print_list, [1, 2, 3, 4], 10)
    print("Result of print_list: {}".format(result))
