# 3. Узнайте у пользователя число n.
# Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3.
# Считаем 3 + 33 + 333 = 369.

n = int(input('Enter n: '))
sum_ = 0
last_step = 3
step = 0
str_n = ''
while step < last_step:
    str_n = str_n + str(n)
    sum_ = sum_ + int(str_n)
    step += 1
print(sum_)
