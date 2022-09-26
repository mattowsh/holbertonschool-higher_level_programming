#!/usr/bin/python3
"""BaseGeometry class"""


class BaseGeometry:
    """Class that define a BaseGeometry object"""
    pass

    def area(self):
        """Calculates the area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates value"""
        # we can assume @name is always a string
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

"""Rectangle class"""


class Rectangle(BaseGeometry):
    """Class based on BaseGeometry baseclass"""

    def __init__(self, width, height):
        """To create a new instance"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Calculates the area of a rectangle"""
        return self.__width * self.__height

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

"""Square class"""
    # Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """Class based on Rectangle baseclass"""

    def __init__(self, size):
        """To create a new instance"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Calculates the area of a square"""
        return self.__size * self.__size
