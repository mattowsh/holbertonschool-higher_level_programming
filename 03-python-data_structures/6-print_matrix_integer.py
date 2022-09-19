#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix is None:
        return

    rows = len(matrix)
    columns = len(matrix[0])

    for i in range(0, rows):
        for j in range(0, columns):
            print("{:d}".format(matrix[i][j]), end="")
            if j != columns - 1:
                print(end=" ")
        print()
