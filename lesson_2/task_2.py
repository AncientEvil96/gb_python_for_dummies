# 2. Для списка реализовать обмен значений соседних элементов, т.е.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

list_1 = list()

while True:
    list_1.append(input('Write element: '))
    answer = input('Introduce more? y/n ')
    if answer == 'n' or answer == 'no':
        break

print('Swap elements')

step = len(list_1) // 2 * 2

i = 0
while i < step:
    old_e = list_1[i]
    list_1[i] = list_1[i+1]
    list_1[i+1] = old_e
    i += 2

print(list_1)
