# Реализовать функцию int_func(), принимающую слова из маленьких латинских букв и возвращающую их же,
# но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
#
# Продолжить работу над заданием.
# В программу должна попадать строка из слов, разделённых пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре.
# Нужно сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
# Используйте написанную ранее функцию int_func().

def int_func(text_):
    text_.lower()
    for i in text_:
        if i not in 'abcdefghijklmnopqrstuvwxyz ':
            print('error: you are using non-latin letters')
            return

    print(f'Answer_1: {text_.capitalize()}')
    print(f'Answer_2: {text_.title()}')


int_func(input("enter latin letters text: "))
