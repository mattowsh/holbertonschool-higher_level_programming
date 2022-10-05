#!/usr/bin/python3
"""
Unittest for class Rectangle methods
"""
import unittest
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
          #  Rectangle(1, "2")
           # Rectangle(1, 2, "3")
          #  Rectangle(1, 2, 3, "4")

    def test_id_ok(self):
        """ check to check id of the class, passed as argument """
        rect = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(rect.id, 5)
