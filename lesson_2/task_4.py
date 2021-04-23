# 4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки.
# Строки необходимо пронумеровать.
# Если в слово длинное, выводить только первые 10 букв в слове.

user_text = input('Write text: ')
list_text = user_text.split(' ')
autoincrement = 1
for i in list_text:
    print(f'{autoincrement},{i[0:9]}')
    autoincrement += 1
