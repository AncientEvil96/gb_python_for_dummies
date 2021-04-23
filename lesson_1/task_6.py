# 6. Спортсмен занимается ежедневными пробежками.
# В первый день его результат составил a километров.
# Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
# Требуется определить номер дня, на который общий результат спортсмена составить не менее b километров.
# Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.
# Например: a = 2, b = 3.
# Результат:
# 1-й день: 2
# 2-й день: 2,2
# 3-й день: 2,42
# 4-й день: 2,66
# 5-й день: 2,93
# 6-й день: 3,22
#
# Ответ: на 6-й день спортсмен достиг результата — не менее 3 км.

first_ = int(input('Enter a: '))
last_ = int(input('Enter b: '))
print(f'1-й день: {first_}')
days = 1
while first_ < last_:
    days += 1
    first_ = first_ * 1.1
    print(f'{days}-й день: {round(first_, 2)}')

print(f'Ответ: на {days}-й день спортсмен достиг результата — не менее {last_} км.')