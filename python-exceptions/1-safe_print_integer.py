#!/usr/bin/python3
def safe_print_integer(value):
    try:
        value_type = isinstance(value, int)
        print("{:d}".format(value))
    except:
        return value_type
    return value_type
