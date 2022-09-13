#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if (len(tuple_a) >= 2) and (len(tuple_b) >= 2):
        fst_sum = tuple_a[0] + tuple_b[0]
        snd_sum = tuple_a[1] + tuple_b[1]

    elif (len(tuple_a) == 0) and (len(tuple_b) == 0):
        fst_sum = snd_sum = 0

    elif (len(tuple_a) == 0):
        fst_sum = tuple_b[0]
        snd_sum = tuple_b[1]

    elif (len(tuple_b) == 0):
        fst_sum = tuple_a[0]
        snd_sum = tuple_a[1]

    elif (len(tuple_a) == 1) or (len(tuple_b) == 1):
        fst_sum = tuple_a[0] + tuple_b[0]
        snd_sum = 0

    print("({:d}, {:d})".format(fst_sum, snd_sum))
