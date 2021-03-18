# Создать текстовый файл (не программно),
# сохранить в нём несколько строк, выполнить подсчёт строк и слов в каждой строке.

with open('test_1.txt', 'r+') as my_f:
    my_f.write(f'\n test test \n test test \n test test')
    my_f.seek(0)
    text_f = my_f.read()
    print(len(text_f.split()))
    print(len(text_f.split('\n')))