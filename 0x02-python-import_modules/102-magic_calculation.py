def magic_calculation(a, b):
    """Match bytecode provided by Holberton School."""
    from magic_calculation_102 import add, sub

    result = 0

    if a < b:
        result = add(a, b)
        for i in range(4, 6):
            result = add(result, i)
    else:
        result = sub(a, b)

    return (result)
