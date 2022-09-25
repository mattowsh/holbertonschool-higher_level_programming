#!/usr/bin/python3

Rectangle = __import__('8-rectangle').Rectangle

my_rectangle_1 = Rectangle(8, 4)
my_rectangle_2 = Rectangle(2, 3)

print(my_rectangle_1 == Rectangle.bigger_or_equal(my_rectangle_1, my_rectangle_2))
