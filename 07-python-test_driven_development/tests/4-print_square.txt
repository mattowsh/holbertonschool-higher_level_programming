Test module: def print_square(size):
------------
This is an example text file in reStructuredText format.
------------

First import ``print_square`` from the ``4-print_square`` module:
>>> print_square = __import__('4-print_square').print_square

Try it:
>>> print_square(5)
#####
#####
#####
#####
#####

>>> print_square(-2)
Traceback (most recent call last):
ValueError: size must be >= 0

>>> print_square()
Traceback (most recent call last):
TypeError: print_square() missing 1 required positional argument: 'size'

>>> print_square("not_a_int")
Traceback (most recent call last):
TypeError: size must be an integer

>>> print_square(3.14)
Traceback (most recent call last):
TypeError: size must be an integer
