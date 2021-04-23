# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def del_n(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        return 'division by 0'


print(f'answer: {del_n(int(input("enter the number x: ")), int(input("enter the number y: ")))}')