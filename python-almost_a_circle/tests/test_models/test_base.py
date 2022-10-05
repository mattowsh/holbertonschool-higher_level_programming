#!/usr/bin/python3
"""
Unittest for class Base methods
"""
import unittest
import json
from models.base import Base


class Test_classBase(unittest.TestCase):
    def test_init_id(self):
        """ test to check the correct creation of a new instance
        and the optimal id value assignment """
        base0 = Base(id=None)
        self.assertEqual(base0.id, 1)

        base1 = Base()
        self.assertEqual(base1.id, 2)

        base2 = Base(-10)
        self.assertEqual(base2.id, -10)

        base3 = Base()
        self.assertEqual(base3.id, 3)

        base4 = Base("string")
        self.assertEqual(base4.id, "string")

        base5 = Base(3.14)
        self.assertEqual(base5.id, 3.14)

        base6 = Base(['love', 'buzz'])
        self.assertEqual(base6.id, ['love', 'buzz'])

        base7 = Base(7**2)
        self.assertEqual(base7.id, 49)

        base8 = Base(1e09)
        self.assertEqual(base8.id, 1e09)

        with self.assertRaises(TypeError):
            Base(2, 4, 5, 8)

        


if __name__ == "__main__":
    unittest.main()
