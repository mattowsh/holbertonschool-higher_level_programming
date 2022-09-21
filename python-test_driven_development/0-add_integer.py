#!/usr/bin/python3
""" Task 0 module """


def add_integer(a, b=98):
    """Adds 2 integers and return the result"""

    if type(a) != int and type(a) != float:
        raise TypeError("a must be an integer")
    if type(b) != int and type(b) != float:
        raise TypeError("b must be an integer")

    if type(a) == float:
        a = int(a)
    if type(b) == float:
        b = int(b)

    return a + b
