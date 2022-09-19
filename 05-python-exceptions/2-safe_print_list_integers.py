#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    counter = 0

    try:
        for i in range(0, x):
            value_type = isinstance(my_list[i], int)
            if value_type != 0:
                print("{:d}".format(my_list[i]), end="")
                counter += 1
    except IndexError:
        raise IndexError
    else:
        print()
        return counter
