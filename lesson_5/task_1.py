# Создать программный файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных будет свидетельствовать пустая строка.

with open('test_1.txt', 'w') as my_f:
    while True:
        text_ = input('Введите текст: ')
        if text_ == '':
            break
        else:
            my_f.write(f'{text_} \n')
