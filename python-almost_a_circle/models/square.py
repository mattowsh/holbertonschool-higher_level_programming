#!/usr/bin/python3
"""
Module that creates a class 'Square' that inherits from class 'Rectangle'
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ New class, inherits from Rectangle """

    def __init__(self, size, x=0, y=0, id=None):
        """ Constructor that creates a new instance """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ Overrides the __str__ method so that it returns a
        personalizated message """
        result = "[Square] ({}) ".format(self.id)
        result += "{}/{} - {}".format(self.x, self.y, self.width)
        return result

    @property
    def size(self):
        """ To get the private size attribute: getter """
        return self.width

    @size.setter
    def size(self, value):
        """ To set the private size attribute: setter """
        self.width = value
        self.height = value
