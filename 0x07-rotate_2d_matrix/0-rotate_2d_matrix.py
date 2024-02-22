#!/usr/bin/python3
"""rotate_2d_matrix
"""


def rotate_2d_matrix(matrix):
    """Given an n x n 2D matrix, rotate it 90 degrees clockwise.
    """
    n = len(matrix)
    temp = [[0] *n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            temp[i][j] = matrix[j][i]

    for i in range(n):
        for j in range(n):
            matrix[i][j] = temp[i][j]
