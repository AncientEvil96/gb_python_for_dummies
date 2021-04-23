# Создать текстовый файл (не программно).
# Построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк).
# Определить, кто из сотрудников имеет оклад менее 20 тысяч, вывести фамилии этих сотрудников.
# Выполнить подсчёт средней величины дохода сотрудников.
# Пример файла:
# Иванов 23543.12
# Петров 13749.32

from os import path
from statistics import mean

my_f_name = 'test_1.txt'
if path.exists(my_f_name):
    with open(my_f_name) as my_f:
        avg_list = []
        for line in my_f:
            line_is_list = line.split()
            avg_list.append(float(line_is_list[1]))
            if float(line_is_list[1]) < 20000:
                print(line_is_list[0])
    print(f'Avg: {mean(avg_list)}')
else:
    print('not file')
