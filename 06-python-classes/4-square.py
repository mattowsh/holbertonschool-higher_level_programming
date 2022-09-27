#!/usr/bin/python3
"""Square class"""


class Square:
    """Class that defines a square with attributes"""
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        """Determinate if the value is or not a int"""
        if isinstance(value, int) == 0:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculates the area of a square"""
        return self.__size * self.__size
