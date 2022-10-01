#!/usr/bin/python3
"""
Module that defines the base class for 'Almost a Circle' project
"""


class Base:
    """Base class with attributes and init constructor"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Constructor that generates a new instance of Base class"""
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
