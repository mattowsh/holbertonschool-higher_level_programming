#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def test_ascend_order_list(self):
        result = max_integer([1, 2, 3, 4])
        self.assertEqual(result, 4)

    def test_descend_order_list(self):
        result = max_integer([4, 3, 2, 1])
        self.assertEqual(result, 4)

    def test_unsorted_list(self):
        result = max_integer([1, 4, 3, 2])
        self.assertEqual(result, 4)

    def test_negative_int(self):
        result = max_integer([-3, -2, -9])
        self.assertEqual(result, -2)

    def test_lenZero(self):
        result = max_integer([])
        self.assertEqual(result, None)

    def test_not_a_list(self):
        result = max_integer([5])
        self.assertEqual(result, 5)
        
    if __name__ == "__main__":
        unittest.main()
