# Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный.
# В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
# Продолжительность первого состояния (красный) составляет 7 секунд,
# второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
# Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
# Проверить работу примера, создав экземпляр и вызвав описанный метод.

from itertools import cycle
import time


class TrafficLight:
    """
    класс TrafficLight предназначенный для работы светофора.

    :param color описаны стандарты цветов сфетофора

    running для запуска
    """
    def __init__(self):
        self.__color = (('red', 7), ('yellow', 2), ('green', 5), ('yellow', 2))

    def running(self):
        print('Start..')
        counter = 0
        for color_, time_step in cycle(self.__color):
            print(color_)
            time.sleep(time_step)

            counter += 1
            if counter == 10:
                print('Stop..')
                break


if __name__ == '__main__':
    traffic_light = TrafficLight()
    traffic_light.running()
