#!/usr/bin/python3

import unittest

from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
          """Set up the SimpleCalculator instance before each test."""
          self.calc = SimpleCalculator()

    def test_addition(self):
         """Test the addition method."""
         self.assertEqual(self.calc.add(2,3),5)
         self.assertEqual(self.calc.add(-1,1),0)
         self.assertEqual(self.calc.add(2,0),2)
         self.assertEqual(self.calc.add(-2,-2),-4)

    def test_subraction(self):
        self.assertEqual(self.calc.subtract(2,2),0)
        self.assertEqual(self.calc.subtract(4,2),2)
        self.assertEqual(self.calc.subtract(-2,1),3)
        self.assertEqual(self.calc.subtract(-3,-4),1)

    def test_muliply(self):
        self.assertEqual(self.calc.multiply(2,3),6)
        self.assertEqual(self.calc.multiply(-2,4),-8)
        self.assertEqual(self.calc.multiply(-2,0),0)
        self.assertEqual(self.calc.multiply(1,1),1)

    def test_divide(self):
        self.assertEqual(self.calc.divide(4,2),2)
        self.assertEqual(self.calc.divide(2,4),0.5)
        self.assertEqual(self.calc.divide(0,5),0)

        self.assertRaises(ValueError,calc.divide, 15,0)


