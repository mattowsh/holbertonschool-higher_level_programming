#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix is None:
        return

    new_list = []
    for i in range(0, len(matrix)):
        square = list(map(lambda x: x*x, matrix[i]))
        new_list.append(square)

    return new_list
