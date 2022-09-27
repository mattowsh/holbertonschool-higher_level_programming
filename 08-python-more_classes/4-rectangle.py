#!/usr/bin/python3
"""Rectangle class"""


class Rectangle:
    """Class that defines a rectangle with attributes"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculates the area of a rectangle"""
        return self.height * self.width

    def perimeter(self):
        """Calculates the perimeter of a rectangle"""
        result = 0
        if self.width != 0 and self.height != 0:
            result = (self.width * 2) + (self.height * 2)
        return result

    def __str__(self):
        """Returns the rectangle in string format"""
        result = ""
        if self.width != 0 and self.height != 0:
            for i in range(self.height):
                result += "#" * self.width
                if i != self.height - 1:
                    result += "\n"

        return result

    def __repr__(self):
        return ("Rectangle({}, {})".format(self.width, self.height))
