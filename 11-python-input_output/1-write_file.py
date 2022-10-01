#!/usr/bin/python3
"""
Task 1 module: writes a string to a text file,
returns the number of characters written, using with statement
"""


def write_file(filename="", text=""):
    """Writes a string to a text file (UTF8) and returns the number
    of characters written"""
    with open(filename, 'w', encoding='utf-8') as file:
        return file.write(text)

    # Note 1: with statement close automatically the file after of use it
    # Note 2: write method return the number of characters written
