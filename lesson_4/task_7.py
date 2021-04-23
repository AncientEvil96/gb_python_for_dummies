# Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
# При вызове функции должен создаваться объект-генератор.
# Функция вызывается следующим образом: for el in fact(n).
# Она отвечает за получение факториала числа.
# В цикле нужно выводить только первые n чисел, начиная с 1! и до n!.
# Подсказка: факториал числа n — произведение чисел от 1 до n. Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.

from math import factorial
from itertools import count

for try_ in count(1):
    try:
        n = int(input(f'try: {try_} Введите конечное число '))
        break
    except ValueError as err:
        print(err)


def fact(n: int):
    for i in range(1, n + 1):
        yield i, factorial(i)


str_text = ''
for i, el in fact(n):
    if i == 1:
        str_text = '1'
    else:
        str_text = f'{str_text} * {i}'
    print(f'{i}! = {str_text} = {el}')
