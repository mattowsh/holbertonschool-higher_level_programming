#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    counter = 0

    try:
        for i in range(0, x):
            print("{:d}".format(my_list[i]), end="")
            counter += 1
    except IndexError:
        print()
    else:
        print()
    finally:
        return counter
