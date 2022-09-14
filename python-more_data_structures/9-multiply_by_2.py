#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    if a_dictionary is None:
        return

    dict_copy = a_dictionary.copy()
    dict_copy.update((key, value*2) for key, value in a_dictionary.items())
    return dict_copy
