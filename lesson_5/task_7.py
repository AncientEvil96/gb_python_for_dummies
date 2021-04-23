# Создать вручную и заполнить несколькими строками текстовый файл,
# в котором каждая строка будет содержать данные о фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1   ООО   10000   5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчёт средней прибыли её не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить её в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджер контекста.

import json
from statistics import mean

with open('test_1.txt', 'w+', encoding='utf-8') as my_f:
    while True:
        text_ = input('Название: ')
        text_ = text_ + ' ' + input('Форма собственности: ')
        text_ = text_ + ' ' + input('Выручка: ')
        text_ = text_ + ' ' + input('Издержки: ')
        my_f.write(f'{text_} \n')
        if input('Закончить ввод? "n/н": ') in ['n', 'н']:
            break

    dic_firm = {}
    avg_list = []
    my_f.seek(0)
    for line in my_f:
        name, form, revenue, costs = line.split()
        profit = int(revenue) - int(costs)
        dic_firm.update({name: profit})
        if profit > 0:
            avg_list.append(profit)

avg_ = 0
if len(avg_list) > 0:
    avg_ = mean(avg_list)

list_firm = [dic_firm, {'average_profit': avg_}]
print(list_firm)

with open("data_file.json", "w", encoding='utf-8') as my_f:
    json.dump(list_firm, my_f)
