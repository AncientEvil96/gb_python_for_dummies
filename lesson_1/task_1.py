# 1. Поработайте с переменными, создайте несколько, выведите на экран,
# запросите у пользователя несколько чисел и строк и сохраните в переменные, выведите на экран.

name = 'Alex'
surname = 'Baserman'
age = 56
gender_m = True
height = 171.4
print(f'My name: {name} {surname} \nMy age: {age} \nMy gender: {gender_m} \nMy height: {height} '
      f'\nI will answer your questions.')

query = input('Write you query: ')
print('Your query: ' + query)
query = int(input('I can add any number to 5, enter the number: '))
print('Your answer: ' + str(5 + query))
