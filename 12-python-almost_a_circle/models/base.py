#!/usr/bin/python3
"""
Module that defines the base class for 'Almost a Circle' project
"""
import json
from os.path import exists


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of a list of dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ Writes the JSON string representation of list_objs to a file """
        filename = cls.__name__ + ".json"
        result = []

        if list_objs is not None:
            for element in list_objs:
                result.append(element.to_dictionary())

        with open(filename, 'w', encoding='utf-8') as file:
            file.write(cls.to_json_string(result))

    @staticmethod
    def from_json_string(json_string):
        """ Return the list of the JSON string representation of a
        list of dictionaries """
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ Returns an instance with all attributes already set,
        using the update method to assign all these attributes """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        if cls.__name__ == "Square":
            dummy = cls(1)

        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """ Returns a list of instances """
        filename = cls.__name__ + ".json"
        instances_list = []

        if exists(filename):
            with open(filename, 'r') as file:
                jsonstring = cls.from_json_string(file.read())
                for element in jsonstring:
                    instances_list.append(cls.create(**element))
        return instances_list
