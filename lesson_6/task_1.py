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
    def __init__(self):
        self.__color = ('red', 'yellow', 'green')

    def running(self):
        print('Start..')
        counter = 0
        for i in cycle(self.__color):
            print(i)
            counter += 1
            if i == 'green':
                time.sleep(5)
            elif i == 'yellow':
                time.sleep(2)
            else:
                time.sleep(7)

            if counter == 20:
                print('Stop..')
                break


if __name__ == '__main__':
    traffic_light = TrafficLight()
    traffic_light.running()
