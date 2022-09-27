#!/usr/bin/python3
""" Task 5 module """


def text_indentation(text):
    """ Prints a text with 2 new lines after each
        of these characters: ., ? and : """
    if type(text) != str:
        raise TypeError("text must be a string")

    find_character = 0
    for i in range(len(text)):
        if text[i] is "." or text[i] is "?" or text[i] is ":":
            print(text[i] + "\n")
            find_character = 1
        if find_character == 1:
            if text[i + 1] == " ":
                continue
            find_character = 0
        else:
            print(text[i], end="")
