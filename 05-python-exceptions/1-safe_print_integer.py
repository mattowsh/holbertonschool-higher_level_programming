#!/usr/bin/python3
def safe_print_integer(value):
    try:
        value_type = isinstance(value, int)
        print("{:d}".format(value))
    except:
        return value_type
    return value_type

    # if the type of value == 2nd parameter in isinstance,
    # this function return True
    # I will entry in except block if value_type is False
