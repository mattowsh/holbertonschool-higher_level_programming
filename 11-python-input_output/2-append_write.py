#!/usr/bin/python3
"""
Task 2 module: Append to a file
"""


def append_write(filename="", text=""):
    """
    Appends a string at the end of a text file (UTF8)
    Return: number of characters added
    """
    with open(filename, 'a', encoding='utf-8') as file:
        return file.write(text)
