import unittest
from main import *

class CalcTests(unittest.TestCase):
    def test_perform_math(self):
        self.assertEqual(perform_math(Operator.Add, 0, 2), 2)
        self.assertEqual(perform_math(Operator.Subtract, 10, 5), 5)
        self.assertEqual(perform_math(Operator.Multiply, 5, 5), 25)
        self.assertEqual(perform_math(Operator.Divide, 10, 2), 5)
    def test_convert_operator(self):
        self.assertEqual(convert('+'), Operator.Add)
        self.assertEqual(convert('-'), Operator.Subtract)
        self.assertEqual(convert('*'), Operator.Multiply)
        self.assertEqual(convert('/'), Operator.Divide)
    def test_parse_input(self):
        maths = ['1 + 1', '2 * 2', '10 / 2', '10 - 6', '10 + 6 / 8 - 2 * 5']
        for item in maths:
            parse_input(item)
        parse_input('+ 3', 0, True)

