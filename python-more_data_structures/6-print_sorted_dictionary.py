#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    if a_dictionary is None:
        return

    new_set = {}
    for key, value in sorted(a_dictionary.items(), key=lambda x: x[0]):
        print("{}: {}".format(key, value))
