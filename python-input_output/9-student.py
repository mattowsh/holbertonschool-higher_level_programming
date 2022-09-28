#!/usr/bin/python3
"""
Task 9 module
"""


class Student():
    """Class Student with attributes"""

    def __init__(self, first_name, last_name, age):
        """To create a new instance"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieves a dictionary representation of a Student instance"""
        return self.__dict__
