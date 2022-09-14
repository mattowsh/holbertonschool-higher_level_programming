#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or len(a_dictionary) == 0:
        return None

    max_value = 0
    key_associated = ""
    for key in a_dictionary:
        if a_dictionary[key] > max_value:
            max_value = a_dictionary[key]
            key_associated = key

    return key_associated
