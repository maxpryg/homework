def calculate(exp: str) -> float:
    """Принимает строку состоящую из числа, оператора и второго числа
    разделенных пробелом. Например ('1 + 1'). Если строка является валидным
    математическим выражением, возвращает его результат"""

    operations = {'+': lambda x, y: x + y,
                  '-': lambda x, y: x - y,
                  '*': lambda x, y: x * y,
                  '/': lambda x, y: x / y
                  }

    expression = exp.split()
    if len(expression) != 3:
        raise FormulaError('Введено недопустимое количество элементов')

    op_1 = expression[0]
    op_2 = expression[2]
    operator = expression[1]

    try:
        op_1 = float(op_1)
        op_2 = float(op_2)
    except ValueError:
        raise FormulaError('Значения невозможно преобразовать к типу float')

    if operator not in '+-*/':
        raise FormulaError('Введен недопустимый оператор')

    return operations[operator](op_1, op_2)


class FormulaError(Exception):
    def __init__(self, message='Передана неправильная строка'):
        self.message = message
        super().__init__(self.message)
