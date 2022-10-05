#!/usr/bin/python3
"""
Unittest for class Base methods
"""
import unittest
import json
from models.base import Base


class Test_classBase(unittest.TestCase):

    def test_auto_id(self):
        """ to check the auto-assignement of an id value """
        base0 = Base(id=None)
        self.assertEqual(base0.id, 1)

        base1 = Base()
        self.assertEqual(base1.id, 2)

    def test_negative_id(self):
        """ to check the assignement of an id negative value """
        base2 = Base(-10)
        self.assertEqual(base2.id, -10)

    def test_strign_id(self):
        """ to check the assignement of an id string value """
        base4 = Base("string")
        self.assertEqual(base4.id, "string")

    def test_float_id(self):
        """ to check the assignement of an id float value """
        base5 = Base(3.14)
        self.assertEqual(base5.id, 3.14)

    def test_list_id(self):
        """ to check the assignement of an id list value """
        base6 = Base(['love', 'buzz'])
        self.assertEqual(base6.id, ['love', 'buzz'])

    def test_math_id(self):
        """ to check the assignement of an id value by math operation"""
        base7 = Base(7**2)
        self.assertEqual(base7.id, 49)

    def test_big_id(self):
        """ to check the assignement of an id big number value """
        base8 = Base(1e09)
        self.assertEqual(base8.id, 1e09)

    def test_multiple_args(self):
        """ to check the correct qty of arguments """
        with self.assertRaises(TypeError):
            Base(2, 4, 5, 8)

        


if __name__ == "__main__":
    unittest.main()
