# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

while True:
    month_ = int(input('Write 1-12: '))
    if 0 < month_ < 13:
        break

seasons = ['зима', 'зима', 'весна', 'весна', 'весна', 'лето', 'лето', 'лето', 'осень', 'осень', 'осень', 'зима']
print(f'Через list: {seasons[month_-1]}')

seasons = {'зима': [1, 2, 12], 'весна': [3, 4, 5], 'лето': [6, 7, 8], 'осень': [9, 10, 11]}

for i in seasons:
    if month_ in seasons[i]:
        print(f'Через dict: {i}')
        break
