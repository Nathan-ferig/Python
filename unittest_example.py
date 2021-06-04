"""
This example aims to show the use of unitest

python -m unittest -v unittest_example.py

"""
import unittest

from doctest_example import factorial
from doctest_example import greatest_common_factor

class TestFactorial(unittest.TestCase):

    def test_positive(self):
        self.assertEqual(
            factorial(5),24)
        self.assertEqual(
            factorial(1),1)
        self.assertEqual(
            factorial(0),1)

    def test_negative(self):
        self.assertRaises(ValueError,
            factorial,-5)

    def test_float(self):
        self.assertRaises(ValueError,
            factorial,5.5)

    def test_overflow(self):
        self.assertRaises(OverflowError,
            factorial,1e100)

class TestGCF(unittest.TestCase):

    def test_equal(self):
        self.assertEqual(
            greatest_common_factor(15,35),5)
        self.assertEqual(
            greatest_common_factor(48,72),24)
        self.assertEqual(
            greatest_common_factor(35,15),5)
        self.assertEqual(
            greatest_common_factor(7,5),1)

    def test_negative(self):
        self.assertRaises(ValueError,
            greatest_common_factor,-5,10)
        self.assertRaises(ValueError,
            greatest_common_factor,5,-10)

    def test_float(self):
        self.assertRaises(ValueError,
            greatest_common_factor,5.5,10)
        self.assertRaises(ValueError,
            greatest_common_factor,5,10.6)

    def test_overflow(self):
        self.assertRaises(OverflowError,
            greatest_common_factor,1e100,10)
        self.assertRaises(OverflowError,
            greatest_common_factor,10,1e100)