# Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить её на экран.


with open('test_1.txt', 'w+') as my_f:
    my_list = [i for i in range(0, 10)]
    my_f.write(' '.join(map(str, my_list)))
    my_f.seek(0)
    my_list = my_f.read().split()
    new_list = [float(i) for i in my_list]
    print(f'Sum: {sum(new_list)}')
