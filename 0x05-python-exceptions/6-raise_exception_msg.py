#!/usr/bin/python3
def raise_exception_msg(message=""):
    """
    Raises a name exception with a given message.

    Args:
        message (str): The message to include in the exception.

    Raises:
        NameError: Always raises a NameError with the specified message.
    """
    raise NameError(message)

# Test case
if __name__ == "__main__":
    try:
        raise_exception_msg("C is fun")
    except NameError as ne:
        print(ne)
