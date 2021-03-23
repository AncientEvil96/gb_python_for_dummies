# Реализовать класс Stationery (канцелярская принадлежность).
# Определить в нем атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.”
# Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
# В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов методы должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:
    """

    общий метод агрегатор параметров

    """
    def __init__(self, title = None):
        self.title = title

    def draw(self):
        print('Запуск отрисовки.')


class Pen(Stationery):

    def draw(self):
        print('Запуск Pen.')


class Pencil(Stationery):

    def draw(self):
        print('Запуск Pencil.')


class Handle(Stationery):

    def draw(self):
        print('Запуск Handle.')


if __name__ == '__main__':
    Pen.draw('Pen')
    Pencil.draw('Pencil')
    Handle.draw('Handle')
