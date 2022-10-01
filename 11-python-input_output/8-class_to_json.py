#!/usr/bin/python3
"""
Task 8 module: Class to JSON
"""


def class_to_json(obj):
    """R the dictionary description with simple data structure for
    JSON serialization of an object"""
    return obj.__dict__
