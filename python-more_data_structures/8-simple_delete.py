#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    if a_dictionary is None:
        return

    if key in a_dictionary:
        del a_dictionary[key]
    return a_dictionary
    # the return contemplates when key is not in a_dictionary
