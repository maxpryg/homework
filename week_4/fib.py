def is_int(func):
    """Вызывает исключение TypeError, если аргумент переданный функции func
    не является целым числом"""
    def wrapper(n):
        if not isinstance(n, int):
            raise TypeError(f'Функции {func.__name__} нужно передавать '
                            f'целое число')
        return func(n)
    return wrapper


@is_int
def fib_generator(n):
    """Принимает количество элементов последовательности Фибоначчи и
    итерируется по элементам последовательности.
    Например fib_generator(3) создаст итератор для 3 элементов
    последовательности 0 1 1"""
    a, b, num = 0, 1, 1
    while True:
        if num > n:
            return
        yield a
        a, b = b, a + b
        num += 1


@is_int
def fib_list(n):
    """Принимает количество элементов последовательности Фибоначчи и
    возвращает список с элементами последовательности.
    Вызов ф-и fib_list(3) вернет список [0, 1, 1]"""
    num_list = [0]
    a, b, num = 0, 1, 1
    while num < n:
        a, b = b, a + b
        num += 1
        num_list.append(a)
    return num_list
