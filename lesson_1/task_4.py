# 4. Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

n = -1
while n < 0:
    n = int(input('Enter positive number n: '))

n = str(n)
i = 0
max_number = 0
while i < len(n):
    next_num = int(n[i])
    if max_number < next_num:
        max_number = next_num
    i += 1

print(f'The max number: {max_number}')
