# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Напишите программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

from os import path

swap_dir = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}

my_f_name = 'test_1.txt'
new_text = ''
if path.exists(my_f_name):
    with open(my_f_name) as my_f:
        for line in my_f:
            line_is_list = line.split()
            line_is_list[0] = swap_dir[line_is_list[0]]
            new_text = new_text + ' '.join(line_is_list) + '\n'

    with open('test_2.txt', 'w') as my_f:
        my_f.write(new_text)

else:
    print('not file')
