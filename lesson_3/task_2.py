# Выполнить функцию, которая принимает несколько параметров,
# описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Осуществить вывод данных о пользователе одной строкой.

def user_(name='', surname='', birthday='', city='', email='', phone=''):
    print(f'name: {name}, surname: {surname}, birthday: {birthday}, city: {city}, email: {email}, phone: {phone}')


user_('Иван', 'Иванов', '01/01/1970', 'Кудыкина гора', 'test@test.ru', '9999999999')