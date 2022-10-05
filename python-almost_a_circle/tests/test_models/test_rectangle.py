#!/usr/bin/python3
"""
Unittest for class Rectangle methods
"""
import unittest
from io import StringIO
import sys
from models.rectangle import Rectangle


class Test_classRectangle(unittest.TestCase):

    def test_multiple_parameters(self):
        """ check the new instance with 2 arguments """
        rect0 = Rectangle(1, 2)
        self.assertEqual(rect0.width, 1)
        self.assertEqual(rect0.height, 2)

        rect1 = Rectangle(1, 2, 3)
        self.assertEqual(rect1.width, 1)
        self.assertEqual(rect1.height, 2)
        self.assertEqual(rect1.x, 3)

        rect2 = Rectangle(1, 2, 3, 4)
        self.assertEqual(rect2.width, 1)
        self.assertEqual(rect2.height, 2)
        self.assertEqual(rect2.x, 3)
        self.assertEqual(rect2.y, 4)

    def test_no_int_args(self):
        """ check if the arguments are not int values """
        with self.assertRaises(TypeError):
            Rectangle("1", 2)
        with self.assertRaises(TypeError):
            Rectangle(1, "2")
        with self.assertRaises(TypeError):
            Rectangle(1, 2, "3")
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, "4")

    def test_id_ok(self):
        """ check the id of the class, passed as argument """
        rect = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(rect.id, 5)

    def test_negative_heigh_and_width(self):
        """ check if height and width are a negative int """
        with self.assertRaises(ValueError):
            Rectangle(-1, 2)
        with self.assertRaises(ValueError):
            Rectangle(1, -2)

    def test_zero_height_and_width(self):
        """ check if height and width are zero """
        with self.assertRaises(ValueError):
            Rectangle(0, 2)
        with self.assertRaises(ValueError):
            Rectangle(1, 0)

    def test_negative_x_and_y(self):
        """ check if x and y are a negative int """
        with self.assertRaises(ValueError):
            Rectangle(1, 2, -3)
        with self.assertRaises(ValueError):
            Rectangle(1, 2, 3, -4)

    def test_area(self):
        """ check the correct functionality of area method """
        rect = Rectangle(2, 2)
        self.assertEqual(rect.area(), 4)

    def test_correct_str(self):
        """ check the correct functionality of __str__ method overrides """
        rect = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(rect.__str__(), '[Rectangle] (5) 3/4 - 1/2')

    def test_display_without_xy(self):
        """ check the correct print of the rectangle """
        # without x and y values
        # creating a temporary output
        temp = StringIO()
        # redirect the output to my temporary output
        sys.stdout = temp
        
        rect0 = Rectangle(1, 2)
        rect0.display()
        self.assertEqual(temp.getvalue(), "#\n#\n")

        # without y value
        temp = StringIO()
        sys.stdout = temp

        rect1 = Rectangle(1, 2, 3)
        rect1.display()
        self.assertEqual(temp.getvalue(), "   #\n   #\n")

        # with x and y values
        temp = StringIO()
        sys.stdout = temp

        rect2 = Rectangle(2, 2, 2, 1)
        rect2.display()
        self.assertEqual(temp.getvalue(), "\n  ##\n  ##\n")




if __name__ == "__main__":
    unittest.main()
