# Программа принимает действительное положительное число x и целое отрицательное число y.
# Выполните возведение числа x в степень y.
# Задание реализуйте в виде функции my_func(x, y).
# При решении задания нужно обойтись без встроенной функции возведения числа в степень.
# Подсказка: попробуйте решить задачу двумя способами.
# Первый — возведение в степень с помощью оператора **.
# Второй — более сложная реализация без оператора **, предусматривающая использование цикла.

def my_func_1(x, y):
    return x ** y


def my_func_2(x, y):
    result = 1
    for i in range(abs(y)):
        result *= x
    if y >= 0:
        return result
    else:
        return 1 / result


x = abs(float(input("enter the number x: ")))

while True:
    y = int(input("enter the number -y: "))
    if y < 0:
        break

print(round(my_func_1(x, y), 5))
print(round(my_func_2(x, y), 5))
