#!/usr/bin/python3
"""
Task 3 module: To JSON string
"""
import json


def to_json_string(my_obj):
    """Return: the JSON representation of an object (string)"""
    if my_obj is None:
        return
    else:
        return json.dumps(my_obj)
