#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    rtn_matrix = [[] for _ in range(len(matrix))]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            rtn_matrix[i].append(matrix[i][j] * matrix[i][j])

    return (rtn_matrix)
