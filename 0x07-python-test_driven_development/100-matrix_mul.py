#!/usr/bin/python3

def matrix_mul(m_a, m_b):
    """Multiply two matrices m_a and m_b.

    Args:
        m_a (list): First matrix (list of lists).
        m_b (list): Second matrix (list of lists).

    Returns:
        list: Resulting matrix after multiplication.

    Raises:
        TypeError: If m_a or m_b is not a list of lists,
                   or if elements of the matrices are not integers or floats,
                   or if the matrices are not rectangular (rows of same size).
        ValueError: If m_a or m_b is empty,
                    or if matrices cannot be multiplied.

    """
    # Validate m_a and m_b
    for matrix in (m_a, m_b):
        if not isinstance(matrix, list):
            raise TypeError("m_a must be a list or m_b must be a list")
        if len(matrix) == 0 or any(not isinstance(row, list) for row in matrix):
            raise ValueError("m_a can't be empty or m_b can't be empty")
        if any(not all(isinstance(num, (int, float)) for num in row) for row in matrix):
            raise TypeError("m_a should contain only integers or floats or m_b should contain only integers or floats")

    # Validate rectangular shape
    num_cols_a = len(m_a[0])
    num_cols_b = len(m_b[0])
    if any(len(row) != num_cols_a for row in m_a) or any(len(row) != num_cols_b for row in m_b):
        raise TypeError("each row of m_a must be of the same size or each row of m_b must be of the same size")

    # Validate multiplication compatibility
    if num_cols_a != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    # Perform matrix multiplication
    result = [[0] * num_cols_b for _ in range(len(m_a))]
    for i in range(len(m_a)):
        for j in range(num_cols_b):
            result[i][j] = sum(m_a[i][k] * m_b[k][j] for k in range(num_cols_a))

    return result
