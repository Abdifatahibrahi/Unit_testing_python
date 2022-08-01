import unittest
import calc
from unittest import TestCase


class TestCalc(TestCase):

    def test_add(self):
        self.assertEqual(calc.add(10,5), 15)
        self.assertEqual(calc.add(10,-5), 5)
        self.assertEqual(calc.add(-10,-5), -15)
        self.assertEqual(calc.add(10.5,5.1), 15.6)

    def test_subtract(self):
        self.assertEqual(calc.subtract(10,5), 5)
        self.assertEqual(calc.subtract(10,-5), 15)
        self.assertEqual(calc.subtract(-10,-5), -5)
        self.assertEqual(calc.subtract(10.5,5.1), 5.4)

    def test_multiply(self):
        self.assertEqual(calc.multiply(10,5), 50)
        self.assertEqual(calc.multiply(10,-5), -50)
        self.assertEqual(calc.multiply(-10,-5), 50)

    def test_divide(self):
        self.assertEqual(calc.divide(10,5), 2)
        self.assertEqual(calc.divide(10,-5), -2)
        self.assertEqual(calc.divide(-10,-5), 2)

        with self.assertRaises(ValueError):
            calc.divide(20, 5)
        
        



if __name__ == '__main__':
    unittest.main()