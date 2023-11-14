#!/usr/bin/python3
"""This module rotates a given 2D matrix clockwise"""


def rotate_2d_matrix(matrix):
    """Rotate a 2D matrix clockwise"""
    n = len(matrix)
    # print(n)

    # Transpose the matrix
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse each row
    for i in range(n):
        matrix[i].reverse()
