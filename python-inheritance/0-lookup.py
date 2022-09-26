#!/usr/bin/python3
def lookup(obj):
    """Returns the list of available attributes and
    methods of an object"""
    if obj is None:
        return

    return dir(obj)
