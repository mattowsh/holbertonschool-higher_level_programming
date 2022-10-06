#!/usr/bin/python3
"""
Unittest for class Square methods
"""
import unittest
from io import StringIO
import sys
from models.square import Square


class Test_classSquare(unittest.TestCase):

    def test_multiple_parameters(self):
        """ check the new instance with many arguments """
        sq0 = Square(1)
        self.assertEqual(sq0.size, 1)

        sq1 = Square(1, 2)
        self.assertEqual(sq1.width, 1)
        self.assertEqual(sq1.height, 1)
        self.assertEqual(sq2.x, 2)

        sq2 = Square(1, 2, 3)
        self.assertEqual(sq2.width, 1)
        self.assertEqual(sq1.height, 1)
        self.assertEqual(sq2.x, 2)
        self.assertEqual(sq2.y, 3)
