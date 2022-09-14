#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    # task definition: key argument will be always a string, so never be None
    if a_dictionary is None:
        return

    a_dictionary[key] = value
    return a_dictionary
