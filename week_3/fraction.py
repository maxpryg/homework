from math import gcd, lcm


class MathMixin():
    """Этот миксин реализует статические методы, для операций вычитание,
    сложение, умножение и деление"""
    @staticmethod
    def add(fract1, fract2):
        # наименьшее общее кратное
        den = lcm(fract1.den, fract2.den)
        num = den // fract1.den * fract1.num + den // fract2.den * fract2.num
        return fract1.__class__(num, den)

    @staticmethod
    def sub(fract1, fract2):
        # наименьшее общее кратное
        den = lcm(fract1.den, fract2.den)
        num = den // fract1.den * fract1.num - den // fract2.den * fract2.num
        return fract1.__class__(num, den)

    @staticmethod
    def mull(fract1, fract2):
        num = fract1.num * fract2.num
        den = fract1.den * fract2.den
        return fract1.__class__(num, den)

    @staticmethod
    def div(fract1, fract2):
        num = fract1.num * fract2.den
        den = fract1.den * fract2.num
        return fract1.__class__(num, den)


class Fraction(MathMixin):
    """Класс реализует представление дробных числел.
    Имеет два атрибута: num - числитель, den -  знаменатель."""
    def __init__(self, num, den):
        self.__num = num
        self.__den = den
        # наибольший общий делитель
        g_c_d = gcd(num, den)
        # сокращаем дробь, если это необходимо
        if g_c_d > 1:
            self.__num //= g_c_d
            self.__den //= g_c_d

    @property
    def num(self):
        return self.__num

    @property
    def den(self):
        return self.__den

    def __str__(self):
        return f"{self.num}/{self.den}"

    def __sub__(self, fract):
        """Вычитание:  2/3 - 1/3 = 1/3"""
        # наименьшее общее кратное
        den = lcm(self.den, fract.den)
        num = den // self.den * self.num - den // fract.den * fract.num
        return self.__class__(num, den)

    def __add__(self, fract):
        """Сложение:  2/5 - 1/5 = 3/5"""
        # наименьшее общее кратное
        den = lcm(self.den, fract.den)
        num = den // self.den * self.num + den // fract.den * fract.num
        return self.__class__(num, den)

    def __mul__(self, fract):
        """Умножение:  2/5 * 1/6 = 1/15"""
        num = self.num * fract.num
        den = self.den * fract.den
        return self.__class__(num, den)

    def __truediv__(self, fract):
        """Деление:  2/5 / 1/6 = 12/5"""
        num = self.num * fract.den
        den = self.den * fract.num
        return self.__class__(num, den)

    @classmethod
    def from_string(cls, string):
        """Создает объект дроби из строки вида 'числитель/знаменатель'"""
        num = int(string.split("/")[0])
        den = int(string.split("/")[1])
        return cls(num, den)


if __name__ == "__main__":
    from random import randint

    def fract_gen(a, b):
        yield (Fraction(randint(a, b), randint(a, b)),
               Fraction(randint(a, b), randint(a, b)))

    for i in range(3):
        for f1, f2 in fract_gen(1, 20):
            print(f"{f1} + {f2} = {f1 + f2}")
            print(f"{f1} - {f2} = {f1 - f2}")
            print(f"{f1} * {f2} = {f1 * f2}")
            print(f"{f1} / {f2} = {f1 / f2}")
            print(f"Fraction.add({f1}, {f2}) = {Fraction.add(f1, f2)}")
            print(f"Fraction.sub({f1}, {f2}) = {Fraction.sub(f1, f2)}")
            print(f"Fraction.mull({f1}, {f2}) = {Fraction.mull(f1, f2)}")
            print(f"Fraction.div({f1}, {f2}) = {Fraction.div(f1, f2)}")
            print("-" * 40)

    print(f"Fraction.from_string('10/100'): {Fraction.from_string('10/100')}")
    print(f"Fraction.from_string('3/300'): {Fraction.from_string('3/300')}")
    print(f"Fraction.from_string('20/101'): {Fraction.from_string('20/101')}")
