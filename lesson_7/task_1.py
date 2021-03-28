# Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц: 3 на 2, 3 на 3, 2 на 4.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса
# Matrix (двух матриц).
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
            line = self.__w_max_m(line, self.max_m_len)

        self.matrix = matrix_lines

    def __w_max_m(self, next_line, size):
        if len(next_line) != size:
            add_count_elem = self.max_m_len - len(next_line)
            while add_count_elem > 0:
                add_count_elem -= 1
                next_line.append(0)
        return next_line

    def __str__(self):
        return '\n'.join(['\t'.join(map(str, i)) for i in self.matrix])

    def __add__(self, other):
        if not isinstance(other, Matrix):
            raise TypeError(f"'{type(other)}' "
                            f"incorrect object type")
        if self.max_m_len > other.max_m_len:
            # выровним матрицу если пришло неровное количество элементов
            for line in other.matrix:
                line = self.__w_max_m(line, self.max_m_len)
        else:
            for line in self.matrix:
                line = self.__w_max_m(line, other.max_m_len)

        result = []

        for item in zip(self.matrix, other.matrix):
            result.append([sum([i, j]) for i, j in zip(*item)])

        return Matrix(result)


if __name__ == '__main__':
    matrix1 = Matrix([[1, 2], [3, 4, 5]])
    print(matrix1, '\n')

    matrix2 = Matrix([[10, 20], [30, 40]])
    print(matrix2, '\n')

    print(matrix1 + matrix2)
