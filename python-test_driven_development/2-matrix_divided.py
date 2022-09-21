#!/usr/bin/python3
""" Task 2 module """


def matrix_divided(matrix, div):
    """Divides all elements of a matrix"""

    # Check: if a matrix is a list
    if type(matrix) != list:
        raise TypeError("matrix must be a matrix (list of lists) "
                        "of integers/floats")

    # Check: if each element of matrix is a list
    # Check: length of each matrix row
    # Check: type of each element in each element of matrix
    for i in range(len(matrix)):
        if type(matrix[i]) != list:
            raise TypeError("matrix must be a matrix (list of lists) "
                            "of integers/floats")
        if i + 1 < len(matrix):
            if len(matrix[i]) != len(matrix[i + 1]):
                raise TypeError("Each row of the matrix must have the "
                                "same size")

        for j in range(len(matrix[0])):
            if type(matrix[i][j]) != int and type(matrix[i][j]) != float:
                raise TypeError("matrix must be a matrix (list of lists) "
                                "of integers/floats")

    # Check: type of divisor
    if type(div) != int and type(div) != float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Finally, return new matrix
    return [list(map(lambda x: round(x / div, 2), elements))
            for elements in matrix]
