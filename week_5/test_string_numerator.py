import unittest
from unittest.mock import patch
import os
from string_numerator import string_numerator


# эти переменные нужны чтобы передавать их в декоратор
# @patch('builtins.input',side_effect=[input_file_name, output_file_name])
input_file_name = 'input.txt'
correct_file_name = 'correct.txt'
output_file_name = 'output.txt'

@patch('builtins.input', side_effect=[input_file_name, output_file_name])
class TestStringNumerator(unittest.TestCase):
    def setUp(self):
        """Создает входящий и правильный(контрольный) тексты, и записывает
        эти тексты в соответствующие файлы"""

        self.input_text = ('Lorem ipsum dolor sit amet, consectetur adipiscing\n'
        'elit, sed do eiusmod tempor incididunt ut labore et dolore magna\n'
        'aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco\n'
        'laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure\n'
        'dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat\n'
        'nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt\n'
        'in culpa qui officia deserunt mollit anim id est laborum.\n')

        self.correct_text = ('1: Lorem ipsum dolor sit amet, consectetur adipiscing\n'
        '2: elit, sed do eiusmod tempor incididunt ut labore et dolore magna\n'
        '3: aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco\n'
        '4: laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure\n'
        '5: dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat\n'
        '6: nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt\n'
        '7: in culpa qui officia deserunt mollit anim id est laborum.\n')

        self.input_file_name = 'input.txt'
        self.correct_file_name = 'correct.txt'
        self.output_file_name = 'output.txt'

        with open(self.input_file_name, 'w') as input_file:
            input_file.write(self.input_text)

        with open(self.correct_file_name, 'w') as correct_file:
            correct_file.write(self.correct_text)

    def tearDown(self):
        """Удаляет все файлы созданные во время тестов"""
        if os.path.exists(self.input_file_name):
            os.remove(self.input_file_name)

        if os.path.exists(self.correct_file_name):
            os.remove(self.correct_file_name)

        if os.path.exists(self.output_file_name):
            os.remove(self.output_file_name)

    def test_output_file_written_correctly(self, mock_inputs):
        """Проверяет правильность записи целевого файла, путем построчного
        сравнение целевого и контрольного файлов"""
        string_numerator()
        with open(self.correct_file_name, 'r') as correct_file,\
                open(self.output_file_name, 'r') as output_file:
            for correct_line, output_line in zip(correct_file, output_file):
                self.assertEqual(correct_line, output_line)

#     @patch('builtins.input', side_effect=[input_file_name, output_file_name])
#     def test_output_file(self, mock_inputs):
#         """Проверяет правильность записи целевого файла, путем построчного
#         сравнение целевого и контрольного файлов"""
#         input_file = self.mock()
#         print(input_file)
#         output_file = self.mock()
#         string_numerator()
#         print(input_file)


if __name__ == '__main__':
    unittest.main()
