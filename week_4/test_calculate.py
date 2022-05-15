import unittest
from calculate import calculate, FormulaError
from random import randint


class TestCalculate(unittest.TestCase):
    def test_wrong_input_length(self):
        with self.assertRaises(FormulaError):
            calculate('2 + 3 + 4')

    def test_cant_convert_to_float(self):
        with self.assertRaises(FormulaError):
            calculate('2 + a')

    def test_wrong_operator(self):
        with self.assertRaises(FormulaError):
            calculate('2 a 3')

    def test_calculate_operations(self):
        for operator in '+-*/':
            for i in range(3):
                self.op_1 = str(randint(1, 20))
                self.op_2 = str(randint(1, 20))
                self.assertEqual(
                    calculate(self.op_1 + operator + self.op_2),
                    float(eval(self.op_1 + operator + self.op_2)))

