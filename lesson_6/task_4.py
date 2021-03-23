# Реализуйте базовый класс Car.
# У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

class Car:
    def __init__(self, speed, color, name, is_police: bool):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'{self.name} started')
        speed_car = 0
        while speed_car < self.speed:
            speed_car += 10
            print(f'car speed: {speed_car}')

    def stop(self):
        self.speed = 0
        print(f'{self.name} stopped')

    def turn(self, direction: int):
        if direction in [-1, 0, 1]:
            ratio = {'-1': 'left', '0': 'forward', '1': 'right'}
            print(f'car turn {ratio[direction]}')

    def show_speed(self):
        print(f'speed car {self.speed}')

    def over_speed(self):
        """
        пропишем сюда отпределенные действия при привышении
        """
        print('Warning! Over speed.')


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            self.over_speed()


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
        print(f'Sport car: restrictions lifted')


class WorkCar(Car):

    def show_speed(self):
        if self.speed > 40:
            self.over_speed()


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
        print(f'Police: {self.is_police}, restrictions lifted')


if __name__ == '__main__':
    sport_car = SportCar(220, 'Red', 'BMW', False)
    sport_car.go()
    sport_car.show_speed()
    sport_car.stop()
    town_car = TownCar(30, 'White', 'Nisan', False)
    town_car.go()
    town_car.show_speed()
    town_car.stop()
    work_car = WorkCar(60, 'Blue', 'Ford', False)
    work_car.go()
    work_car.show_speed()
    work_car.stop()
    police_car = PoliceCar(110, 'Blue', 'Lada', True)
    police_car.go()
    police_car.show_speed()
    police_car.stop()
