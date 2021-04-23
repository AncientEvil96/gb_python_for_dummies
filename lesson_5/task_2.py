# Создать текстовый файл (не программно),
# сохранить в нём несколько строк, выполнить подсчёт строк и слов в каждой строке.

from os import path

my_f_name = 'test_1.txt'

if path.exists(my_f_name):
    with open(my_f_name, 'a+') as my_f:
        my_f.write(f'\n test test \n test test \n test test')
        my_f.seek(0)
        text_f = my_f.read()
        print(f'Words: {len(text_f.split())}')
        lines = len(text_f.split('\n'))
        print(f"Lines: {lines}")
else:
    print('not file')
