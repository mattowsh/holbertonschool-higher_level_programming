#!/usr/bin/python3
"""
Module that creates a class 'Rectangle' that inherits from class 'Base'
"""
from models.base import Base


class Rectangle(Base):
    """ New class, inherits from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Constructor that creates a new instance """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ To get the private width attribute: getter """
        return self.__width

    @width.setter
    def width(self, value):
        """ To set the private width attribute: setter """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ To get the private height attribute: getter """
        return self.__height

    @height.setter
    def height(self, value):
        """ To set the private height attribute: getter """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ To get the private x attribute: getter """
        return self.__x

    @x.setter
    def x(self, value):
        """ To set the private x attribute: getter """
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ To get the private y attribute: getter """
        return self.__y

    @y.setter
    def y(self, value):
        """ To set the private y attribute: getter """
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ Calculates the area of a rectangle """
        return self.__width * self.__height
