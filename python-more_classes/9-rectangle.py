#!/usr/bin/python3
"""Rectangle class"""


class Rectangle:
    """Class that defines a rectangle to create a new instance"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculates the area of a rectangle"""
        return self.height * self.width

    def perimeter(self):
        """Calculates the perimeter of a rectangle"""
        result = 0
        if self.width != 0 and self.height != 0:
            result = (self.width * 2) + (self.height * 2)
        return result

    def __str__(self):
        """Returns the rectangle in string format"""
        result = ""
        if self.width != 0 and self.height != 0:
            for i in range(self.height):
                result += str(self.print_symbol) * self.width
                if i != self.height - 1:
                    result += "\n"
        return result

    def __repr__(self):
        """Returns the rectangle in Python expression format"""
        return ("Rectangle({}, {})".format(self.width, self.height))

    def __del__(self):
        """Deletes a Rectangle instances"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Compares the area of two differents Rectangle instances"""
        if isinstance(rect_1, Rectangle) == 0:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if isinstance(rect_2, Rectangle) == 0:
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """Returns a new Rectangle instance with width == height == size"""
        return cls(size, size)
    # >>>> cls takes the class Rectangle as a parameter <<<<
    # >>>> we represent that the method belongs to the class <<<<
