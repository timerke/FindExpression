"""Задание.
Написать программу на любом языке программирования, которая поместит + (2+3),
- (3-2), или ничего ( ) в промежутках между цифрами от 9 до 0 (в таком порядке)
так, чтобы в результате получилось 200. Например: 98+76-5+43-2-10=200."""

NUMBERS = '9876543210'


def solve_task(required_result):
    """Функция для поиска математического выражения, которое даст требуемый
    результат.
    :param required_result: требуемый результат математического выражения.
    :return: множество всех выражений, приводящих к требуемому результату."""

    result_expressions = set()

    def make_combinations(i_0, expression):
        """В строку с числами от 9 до 0 вставляем знаки + и - во всевозможные
        позиции.
        :param i_0: начальный индекс в строке, где стоит цифра, после которой
        можно поместить + или -;
        :param expression: строка из чисел и знаков + и -, в которую поместим
        очередной знак."""

        i_max = len(expression)
        for i in range(i_0 + 1, i_max):
            for sign in ('+', '-'):
                exp_new = expression[:i] + sign + expression[i:]
                result = eval(f'{exp_new}')
                if result == 200:
                    result_expressions.add(exp_new)
                if exp_new[i + 1] == '0':
                    return 0
                make_combinations(i + 1, exp_new)

    for i in range(len(NUMBERS)):
        exp = NUMBERS[:]
        make_combinations(i, exp)
    return result_expressions


# Получаем все математические выражения
expressions = solve_task(200)
# Выводим математические выражения на экран
for expression in expressions:
    print(f'{expression}={eval(expression)}')
