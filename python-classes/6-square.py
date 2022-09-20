#!/usr/bin/python3
"""Square class"""


class Square:
    """Class that defines a square with attributes"""
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) != tuple and len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[0]) != int or type(value[1]) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculates the area of a square"""
        return self.__size * self.__size

    def my_print(self):
        """Prints the square with the # character"""
        if self.__position[1] > 0:
            for i in range(0, self.__position[1]):
                print()

        if self.__size != 0:
            for i in range(0, self.__size):
                for i in range(0, self.__position[0]):
                    print(" ", end="")
                for j in range(0, self.__size):
                    print("#", end="")
                print()
        else:
            print()
