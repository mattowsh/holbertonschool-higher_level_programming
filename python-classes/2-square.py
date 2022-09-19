#!/usr/bin/python3
"""Square class"""


class Square:
    """Class that defines a square with attributes"""
    def __init__(self, size=0):
        self.__size = size

        if isinstance(size, int) == 0:
            raise TypeError("size must be an integer")
        if size <= 0:
            raise ValueError("size must be >= 0")
