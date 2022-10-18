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

    def update(self, *args, **kwargs):
        """ Assigns an argument to each attribute """
        if len(args) >= 1:
            self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "size":
                    self.size = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

    def to_dictionary(self):
        """ Returns the dictionary representation of a Square """
        return {'id': self.id, 'size': self.width, 'x': self.x, 'y': self.y}
