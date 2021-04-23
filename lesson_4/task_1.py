# Реализовать скрипт, в котором должна быть предусмотрена функция расчёта заработной платы сотрудника.
# Используйте в нём формулу: (выработка в часах*ставка в час) + премия.
# Во время выполнения расчёта для конкретных значений необходимо запускать скрипт с параметрами.

from sys import argv


def result_salary():
    hour, rate, bonus = argv[1:]
    try:
        return int(hour) * int(rate) + int(bonus)
    except ValueError as err:
        print(err)


if __name__ == '__main__':
    print(f'{result_salary()}')
