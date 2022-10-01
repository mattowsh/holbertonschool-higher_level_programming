#!/usr/bin/python3
"""
Task 0 module: reads a text file and prints it using with statement
"""


def read_file(filename=""):
    """Reads a text file (UTF8) and prints it to stdout"""
    with open(filename, 'r', encoding='utf-8') as file:
        print(file.read(), end="")
