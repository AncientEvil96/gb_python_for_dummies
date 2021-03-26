# Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц: 3 на 2, 3 на 3, 2 на 4.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц).
# Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы
# складываем с первым элементом первой строки второй матрицы и т.д.

class Matrix:
    def __init__(self, matrix_lines):
        matrix_lines = matrix_lines
        # найдем макс длинну матрицы
        len_lines = [len(i) for i in matrix_lines]
        self.max_m_len = max(len_lines)
        # выровним матрицу если пришло неровное количество элементов
        for line in matrix_lines:
            if len(line) != self.max_m_len:
                add_count_elem = self.max_m_len - len(line)
                while add_count_elem > 0:
                    add_count_elem -= 1
                    line.append(0)

        self.matrix = matrix_lines

        # if len(line_m) == 1:
        #     self.matrix =
        #     self.line_m = line_m
        #     self.len_mat = len(line_m)
        # else
        #     return 'error elements matrix'

    # def __add__(self, other):
    #     pass


if __name__ == '__main__':
    matrix1 = Matrix([[1, 2, 5], [3, 4]])
    print(matrix1.matrix, '\n')
