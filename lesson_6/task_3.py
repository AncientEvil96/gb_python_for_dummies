# Реализовать базовый класс Worker (работник),
# в котором определить атрибуты: name, surname, position (должность), income (доход).
# Последний атрибут должен быть защищенным и ссылаться на словарь,
# содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
# Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии
# (get_total_income).
# Проверить работу примера на реальных данных
# (создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).

class Worker:
    def __init__(self):
        self.name = 'Ivan'
        self.surname = 'Ivanov'
        self.position = 'Runner in the sun'
        self._income = {'wage': 5000, 'bonus': 10000}


class Position(Worker):
    def __init__(self):
        super().__init__()

    def get_full_name(self):
        self.full_name = f'{self.surname} {self.name}'

    def get_total_income(self):
        self.full_salary = self._income['wage'] + self._income['bonus']


if __name__ == '__main__':
    position = Position()
    position.get_full_name()
    position.get_total_income()
    print(f'worker: {position.full_name}, salary: {position.full_salary}')
