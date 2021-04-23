# Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти чётные числа от 100 до 1000 (включая границы).
# Нужно получить результат вычисления произведения всех элементов списка.
# Подсказка: использовать функцию reduce().

from functools import reduce

def my_composition(res_, i):
    return res_*i

print(reduce(my_composition,[i for i in range(100, 1001, 2)]))


# чисто для себя 2 вариант
res_i = 1
for i in range(100, 1001, 2):
    res_i = (lambda *args: res_i * i)(res_i, i)

print(res_i)
