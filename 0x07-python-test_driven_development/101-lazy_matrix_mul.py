#!/usr/bin/python3
"""Module to perform matrix multiplication using NumPy"""

import numpy as np

def lazy_matrix_mul(m_a, m_b):
    """Multiplies two matrices using NumPy arrays.

    Args:
        m_a (list of lists): First matrix
        m_b (list of lists): Second matrix

    Returns:
        list of lists: Resultant matrix after multiplication

    Raises:
        TypeError: If input matrices are not valid or contain invalid elements
        ValueError: If matrices cannot be multiplied
    """
    # Validate input types
    if not isinstance(m_a, list) or not isinstance(m_b, list):
        raise TypeError("m_a must be a list or m_b must be a list")

    # Validate list of lists structure
    if not all(isinstance(row, list) for row in m_a) or not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_a must be a list of lists or m_b must be a list of lists")

    # Validate non-empty matrices
    if any(len(row) == 0 for row in m_a) or any(len(row) == 0 for row in m_b):
        raise ValueError("m_a can't be empty or m_b can't be empty")

    # Validate element types (int or float)
    if not all(isinstance(num, (int, float)) for row in m_a for num in row) or not all(isinstance(num, (int, float)) for row in m_b for num in row):
        raise TypeError("m_a should contain only integers or floats or m_b should contain only integers or floats")

    # Validate consistent row sizes
    if any(len(row) != len(m_a[0]) for row in m_a) or any(len(row) != len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_a must be of the same size or each row of m_b must be of the same size")

    # Perform matrix multiplication using NumPy
    try:
        result = np.matmul(m_a, m_b)
        return (result.tolist())
    except ValueError:
        raise ValueError("m_a and m_b can't be multiplied")

# Uncomment the following block for inline doctests
'''
if __name__ == "__main__":
    import doctest
    doctest.testmod()
'''
