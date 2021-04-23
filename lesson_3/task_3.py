# Реализовать функцию my_func(),
# которая принимает три позиционных аргумента и возвращает сумму наибольших двух аргументов.

def my_func(*args):
    max_full = list(args)
    max_full.sort()
    max_1, max_2 = max_full[-1], max_full[-2]

    return max_1 + max_2


print(my_func(10, 20, 30))