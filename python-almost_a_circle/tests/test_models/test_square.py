#!/usr/bin/python3
"""
Unittest for class Square methods
"""
import unittest
from io import StringIO
import sys
from models.square import Square


class Test_classSquare(unittest.TestCase):

    def test_one_parameter(self):
        """ check the new instance with one argument """
        sq0 = Square(1)
        self.assertEqual(sq0.size, 1)

    def test_multiple_parameter(self):
        """ check the new instance with multiple arguments """
        sq1 = Square(1, 2)
        self.assertEqual(sq1.width, 1)
        self.assertEqual(sq1.height, 1)
        self.assertEqual(sq1.x, 2)

        sq2 = Square(1, 2, 3)
        self.assertEqual(sq2.width, 1)
        self.assertEqual(sq2.height, 1)
        self.assertEqual(sq2.x, 2)
        self.assertEqual(sq2.y, 3)

        sq3 = Square(1, 2, 3, 4)
        self.assertEqual(sq3.width, 1)
        self.assertEqual(sq3.height, 1)
        self.assertEqual(sq3.x, 2)
        self.assertEqual(sq3.y, 3)
        self.assertEqual(sq3.id, 4)

    def test_no_int_args(self):
        """ check if the arguments are not int values """
        with self.assertRaises(TypeError):
            Square("1", 2)
        with self.assertRaises(TypeError):
            Square(1, "2")
        with self.assertRaises(TypeError):
            Square(1, 2, "3")
