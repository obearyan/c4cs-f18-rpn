import unittest

import rpn

class TestBasics(unittest.TestCase):
    def test_add(self):
        result = rpn.calculate("1 1 +")
        self.assertEqual(2, result)
    def test_subtract(self):
        result = rpn.calculate("5 3 -")
        self.assertEqual(2, result)
    def test_multiply(self):
        result = rpn.calculate("5 3 *")
        self.assertEqual(15, result)
    def test_divide(self):
        result = rpn.calculate("6 3 /")
        self.assertEqual(2, result)
    def test_carat(self):
        result = rpn.calculate("2 3 ^")
        self.assertEqual(8, result)
    def test_intdivision(self):
        result = rpn.calculate("5 3 //")
        self.assertEqual(1, result)
    def test_percentages(self):
        result = rpn.calculate("72 5 %")
        self.assertEqual(75.6, result)
    def test_bitwiseand(self):
        result = rpn.calculate("15 11 &")
        self.assertEqual(11, result)
    def test_bitwiseor(self):
        result = rpn.calculate("1 14 |")
        self.assertEqual(15, result)
    def test_bitwisenot(self):
        result = rpn.calculate("3 ~")
        self.assertEqual((-4), result)
    def test_factorial(self):
        result = rpn.calculate("4 !")
        self.assertEqual(24, result)

