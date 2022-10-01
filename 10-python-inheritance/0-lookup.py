#!/usr/bin/python3
"""Lookup function"""


def lookup(obj):
    """Returns the list of available attributes and
    methods of an object"""
    if obj is None:
        return

    return dir(obj)
