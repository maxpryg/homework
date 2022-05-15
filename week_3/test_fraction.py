import unittest
from fraction import Fraction


class TestFraction(unittest.TestCase):
    def setUp(self):
        # создать две дроби
        self.f1 = Fraction(3, 4)
        self.f2 = Fraction(5, 6)

    def test_fraction_values(self):
        """Проверка числителя и знаменателя точек"""
        self.assertEqual(self.f1.num, 3)
        self.assertEqual(self.f1.den, 4)
        self.assertEqual(self.f2.num, 5)
        self.assertEqual(self.f2.den, 6)

    def test_fraction_reduction(self):
        """Проверка сокращения дробей при создании"""
        self.f3 = Fraction(32, 40)
        self.f4 = Fraction(50, 60)
        self.assertEqual(self.f3.num, 4)
        self.assertEqual(self.f3.den, 5)
        self.assertEqual(self.f4.num, 5)
        self.assertEqual(self.f4.den, 6)

    def test_fraction_from_string(self):
        """Проверка создания дроби из строки"""
        self.f1 = Fraction.from_string('3/4')
        self.f2 = Fraction.from_string('5/6')
        self.assertEqual(self.f1.num, 3)
        self.assertEqual(self.f1.den, 4)
        self.assertEqual(self.f2.num, 5)
        self.assertEqual(self.f2.den, 6)

    def test_string_represantation(self):
        """Проверка строкового представления дробей"""
        self.assertEqual(str(self.f1), '3/4')
        self.assertEqual(str(self.f2), '5/6')

    def test_addition(self):
        """Проверка сложения. Проверка реализована путем сравнения числителя
        и знаменателя, а также строкового представления дробей. Так как методы
        сравнения в классе Fraction не реализованы."""
        self.f_add = self.f1 + self.f2
        self.assertEqual(self.f_add.num, 19)
        self.assertEqual(self.f_add.den, 12)
        self.assertEqual(str(self.f_add), '19/12')

    def test_substraction(self):
        """Проверка вычитания. Проверка реализована путем сравнения числителя
        и знаменателя, а также строкового представления дробей. Так как методы
        сравнения в классе Fraction не реализованы."""
        self.f_sub = self.f1 - self.f2
        self.assertEqual(self.f_sub.num, -1)
        self.assertEqual(self.f_sub.den, 12)
        self.assertEqual(str(self.f_sub), '-1/12')

    def test_multiplication(self):
        """Проверка умножения. Проверка реализована путем сравнения числителя
        и знаменателя, а также строкового представления дробей. Так как методы
        сравнения в классе Fraction не реализованы."""
        self.f_mul = self.f1 * self.f2
        self.assertEqual(self.f_mul.num, 5)
        self.assertEqual(self.f_mul.den, 8)
        self.assertEqual(str(self.f_mul), '5/8')

    def test_division(self):
        """Проверка деления. Проверка реализована путем сравнения числителя
        и знаменателя, а также строкового представления дробей. Так как методы
        сравнения в классе Fraction не реализованы."""
        self.f_div = self.f1 / self.f2
        self.assertEqual(self.f_div.num, 9)
        self.assertEqual(self.f_div.den, 10)
        self.assertEqual(str(self.f_div), '9/10')

    def test_mixin_addition(self):
        """Проверка сложения через методы миксин класса. Проверка реализована
        путем сравнения числителя и знаменателя, а также строкового
        представления дробей. Так как методы сравнения в классе Fraction не
        реализованы."""
        self.f_add = Fraction.add(self.f1, self.f2)
        self.assertEqual(self.f_add.num, 19)
        self.assertEqual(self.f_add.den, 12)
        self.assertEqual(str(self.f_add), '19/12')

    def test_mixin_substraction(self):
        """Проверка вычитания через методы миксин класса. Проверка реализована
        путем сравнения числителя и знаменателя, а также строкового
        представления дробей. Так как методы сравнения в классе Fraction не
        реализованы."""
        self.f_sub = self.f1 - self.f2
        self.assertEqual(self.f_sub.num, -1)
        self.assertEqual(self.f_sub.den, 12)
        self.assertEqual(str(self.f_sub), '-1/12')

    def test_mixin_multiplication(self):
        """Проверка умножения через методы миксин класса. Проверка реализована
        путем сравнения числителя и знаменателя, а также строкового
        представления дробей. Так как методы сравнения в классе Fraction не
        реализованы."""
        self.f_mul = self.f1 * self.f2
        self.assertEqual(self.f_mul.num, 5)
        self.assertEqual(self.f_mul.den, 8)
        self.assertEqual(str(self.f_mul), '5/8')

    def test_mixin_division(self):
        """Проверка деления через методы миксин класса. Проверка реализована
        путем сравнения числителя и знаменателя, а также строкового
        представления дробей. Так как методы сравнения в классе Fraction не
        реализованы."""
        self.f_div = self.f1 / self.f2
        self.assertEqual(self.f_div.num, 9)
        self.assertEqual(self.f_div.den, 10)
        self.assertEqual(str(self.f_div), '9/10')


if __name__ == "__main__":
    unittest.main()
