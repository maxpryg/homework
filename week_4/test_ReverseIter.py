import unittest
from ReverseIter import ReverseIter
from collections.abc import Iterator


class TestReverseIter(unittest.TestCase):
    def test_input_data_is_list(self):
        self.ri = ReverseIter(['a', 'b', 'c'])
        self.assertIsInstance(self.ri.data, list)

    def test_input_data_is_string(self):
        with self.assertRaises(TypeError):
            ReverseIter('abc')

    def test_input_data_is_int(self):
        with self.assertRaises(TypeError):
            ReverseIter(123)

    def test_input_data_is_tuple(self):
        with self.assertRaises(TypeError):
            ReverseIter(tuple())

    def test_input_data_is_dict(self):
        with self.assertRaises(TypeError):
            ReverseIter(dict())

    def test_input_data_is_set(self):
        with self.assertRaises(TypeError):
            ReverseIter(set())

    def test_if_object_is_iterator(self):
        self.ri = ReverseIter(list('abcdefg'))
        self.assertIsInstance(self.ri, Iterator)

    def test_correct_iteration_order(self):
        self.data = list('abcdefgh')
        # нужно копировать список, так как это изменяемый объект и он изменится
        # когда будет развернут в обратном порядке
        self.ri = ReverseIter(self.data[:])
        # перевернуть список
        self.data.reverse()
        for r, d in zip(iter(self.ri), self.data):
            self.assertEqual(r, d)


if __name__ == '__main__':
    unittest.main()
