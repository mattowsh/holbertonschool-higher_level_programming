#!/usr/bin/python3
""" Task 4 module """


def print_square(size):
    """ Prints a square with the character # """

    if type(size) != int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
