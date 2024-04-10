#!/usr/bin/python3
"""
Module: 2-matrix_divided

This module defines a function `matrix_divided` that divides all elements of a matrix.

"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a divisor.

    Parameters:
    matrix (list of lists): The matrix containing integers or floats.
    div (int or float): The divisor used for division.

    Raises:
    TypeError: If `matrix` is not a list of lists of integers/floats,
               or if each row of the matrix is not of the same size,
               or if `div` is not a number.
    ZeroDivisionError: If `div` is equal to 0.

    Returns:
    list of lists: A new matrix where all elements are divided by `div` and rounded to 2 decimal places.
    """
    if (not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix)):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    row_size = len(matrix[0])  # Check size of first row
    if not all(len(row) == row_size for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [[round(elem / div, 2) for elem in row] for row in matrix]
    return (new_matrix)
