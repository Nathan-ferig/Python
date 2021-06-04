"""
This example aims to show the use of unitest

python -m unittest -v unittest_example.py

"""
import unittest

from doctest_example import factorial

class TestFactorial(unittest.TestCase):

    def test_positive(self):
        self.assertEqual(
            factorial(5),
            24
        )

    def test_positive(self):
        self.assertEqual(
            factorial(1),
            1
        )

    def test_positive(self):
        self.assertEqual(
            factorial(0),
            1
        )

    def test_negative(self):
        self.assertRaises(ValueError,
            factorial,-5)

    def test_negative(self):
        self.assertRaises(ValueError,
            factorial,-5)

    def test_float(self):
        self.assertRaises(ValueError,
            factorial,5.5)

    def test_overflow(self):
        self.assertRaises(OverflowError,
            factorial,1e100)