#!/usr/bin/python3
for i in range(0, 9):
    for j in range(i + 1, 10):
        if (i != 8 and j != 9):
            print("%s%s" % (i, j), end=", ")
        else:
            print("%s%s" % (i, j))