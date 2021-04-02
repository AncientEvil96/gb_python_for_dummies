"""
== Лото ==

Правила игры в лото.

Игра ведется с помощью специальных карточек, на которых отмечены числа,
и фишек (бочонков) с цифрами.

Количество бочонков — 90 штук (с цифрами от 1 до 90).

Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр,
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:

--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86
--------------------------

В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается
случайная карточка.

Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.

Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
    Если цифра есть на карточке - она зачеркивается и игра продолжается.
    Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
    Если цифра есть на карточке - игрок проигрывает и игра завершается.
    Если цифры на карточке нет - игра продолжается.

Побеждает тот, кто первый закроет все числа на своей карточке.

Пример одного хода:

Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71
--------------------------
-- Карточка компьютера ---
 7 87     - 14    11
      16 49    55 88    77
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)

Подсказка: каждый следующий случайный бочонок из мешка удобно получать
с помощью функции-генератора.

Подсказка: для работы с псевдослучайными числами удобно использовать
модуль random: http://docs.python.org/3/library/random.html

"""

import random


class Gamers:
    def __init__(self, name: str, surname: str):
        self._name = name
        self._surname = surname

    def __str__(self):
        return f'{self._name} {self._surname}'

    def full_name(self):
        return f'{self._name} {self._surname}'


class Game(Gamers):
    def __init__(self, name, surname, complexity: int):
        super().__init__(name, surname)
        self.complexity = 10 * abs(complexity) if complexity in [i for i in range(1, 11)] else 100
        self.__line = 3
        self.__column = 5
        self.__max_column = 9
        self.__user_cart = self.__new_cart()
        self.__pc_cart = self.__new_cart()

    def __new_cart(self):
        new_cart_random = random.sample(range(1, 90), self.__column * self.__line)

        __cart_list = [[new_cart_random.pop() for _ in range(0, self.__column)] for _ in range(0, self.__line)]
        for line in __cart_list:
            line.sort()
            zero_index = [random.randint(1, self.__max_column) for _ in range(0, self.__max_column - self.__column)]
            line = [line.insert(i, '') for i in zero_index]
        return __cart_list

    def start(self):
        range_barrel = [i for i in range(1, 91)]
        while True:
            barrel = random.choice(range_barrel)
            range_barrel.remove(barrel)

            answer = input(f'Новый бочонок: {barrel} (осталось {len(range_barrel)}) \n-------'
                           f' Ваша карточка ------\n{Game.cart_create_print(self.__user_cart)}\n----------------------'
                           f'-----\n--- Карточка компьютера ---\n{Game.cart_create_print(self.__pc_cart)}\n-----------'
                           f'----------------\n Зачеркнуть цифру? (y/n)')

            while answer not in ['y', 'n']:
                answer = input('Неправильно введен вариант ответа, введите еще раз: ')

            leave = False
            for line in self.__user_cart:
                if line.count(barrel) > 0 and answer == 'y':
                    line[line.index(barrel)] = '--'
                    break
                elif (line.count(barrel) > 0 and answer == 'n') or (line.count(barrel) == 0 and answer == 'y'):
                    print(f'{self.full_name()}, lose!')
                    leave = True
                    break

            if leave:
                break

            if self.complexity != 100 and random.randint(0, self.complexity) == 0:
                print(f'{self.full_name()}, win. PC, lose.')
                break

            for line in self.__pc_cart:
                if line.count(barrel) > 0:
                    line[line.index(barrel)] = '--'
                    break

            pc_cart_el = []
            pc_cart_el = [pc_cart_el + [i for i in line if i not in ['', '--']] for line in self.__pc_cart]
            user_cart_el = []
            user_cart_el = [user_cart_el + [i for i in line if i not in ['', '--']] for line in self.__user_cart]

            if len(range_barrel) == 0:
                print('bag, contact the administrator')
                break
            elif len(pc_cart_el) == 0:
                print('pc, win!')
                break
            elif len(user_cart_el) == 0:
                print(f'{self.full_name()}, win')
                break

    @staticmethod
    def cart_create_print(data):
        cart = '\n'.join(
            [''.join([str(i).rjust(3, ' ') for i in line]) for line in data])
        return cart


game = Game('Ivan', 'Ivanov', 0)
game.start()
