#!/usr/bin/python3
"""
    A module to divide a matrix by a specified number
"""

def matrix_divided(matrix, div):
    """
    matrix_divided - divides the matrix
    Args:
        matrix: list of lists containing int or float
        b: int or float

    Returns:
        list of lists: the result of the divison
    """
    if div == 0:
        raise ZeroDivisionError("division by zero")

    if isinstance(matrix, list) is False:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if isinstance(matrix[0], list) is False:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if isinstance(matrix[i][j], (int, float)) is False:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    len_0 = len(matrix[0])
    i = 0
    rtn = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
    while i < len(matrix):
        if len_0 != len(matrix[i]):
            raise TypeError("Each row of the matrix must have the same size")

        for j in range(len(matrix[0])):
            rtn[i][j] = round(matrix[i][j] / div, 2)
        i += 1

    return(rtn)
