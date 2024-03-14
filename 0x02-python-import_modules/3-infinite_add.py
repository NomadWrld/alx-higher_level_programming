#!/usr/bin/python3

if __name__ == "__main__":
    """Print the addition of all arguments."""
    import sys

    # Skip the script name in sys.argv and convert all arguments to integers
    numbers = [int(arg) for arg in sys.argv[1:]]

    # Calculate the sum using the sum() function
    total = sum(numbers)

    # Print the total sum
    print("{}".format(total))
