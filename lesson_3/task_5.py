# Программа запрашивает у пользователя строку чисел, разделённых пробелом.
# При нажатии Enter должна выводиться сумма чисел.
# Пользователь может продолжить ввод чисел, разделённых пробелом и снова нажать Enter.
# Сумма вновь введённых чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введён после нескольких чисел,
# то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.


user_list = []

while True:
    user_list.extend(input('enter number across " ", if exit enter "q": ').split())
    ext_q = user_list.count('q')
    if ext_q > 0:
        index_q = user_list.index('q')
        user_list = user_list[:index_q]
        user_list = [int(i) for i in user_list]
        break
    else:
        user_list = [int(i) for i in user_list]
        print(sum(user_list))

print(sum(user_list))
