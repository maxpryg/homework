import unittest
from fib import fib_generator, fib_list
from collections.abc import Iterator


class TestCalculate(unittest.TestCase):
    def test_fib_generator_is_iterator(self):
        self.fib_gen = fib_generator(9)
        self.assertIsInstance(self.fib_gen, Iterator)

    def test_fib_generator_calculations(self):
        self.fib_gen = fib_generator(9)
        self.fib_list = [0, 1, 1, 2, 3, 5, 8, 13, 21]
        for g, l in zip(self.fib_gen, self.fib_list):
            self.assertEqual(g, l)

    def test_fib_list_calculations(self):
        self.assertEqual(fib_list(1), [0])
        self.assertEqual(fib_list(2), [0, 1])
        self.assertEqual(fib_list(3), [0, 1, 1])
        self.assertEqual(fib_list(4), [0, 1, 1, 2])
        self.assertEqual(fib_list(5), [0, 1, 1, 2, 3])
        self.assertEqual(fib_list(6), [0, 1, 1, 2, 3, 5])
        self.assertEqual(fib_list(7), [0, 1, 1, 2, 3, 5, 8])
        self.assertEqual(fib_list(8), [0, 1, 1, 2, 3, 5, 8, 13])
        self.assertEqual(fib_list(9), [0, 1, 1, 2, 3, 5, 8, 13, 21])


if __name__ == '__main__':
    unittest.main()
