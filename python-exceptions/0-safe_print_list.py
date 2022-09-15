#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    length = 0
    length = sum(1 for item in my_list)

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
