# 2. Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

seconds = int(input('Enter the time in seconds: '))
hours = seconds // 3600
seconds = seconds - hours * 3600
minutes = seconds // 60
seconds = seconds - minutes * 60
seconds = seconds % 3600
hours_format = '{0:0{width}}'.format(hours, width=2)
minutes_format = '{0:0{width}}'.format(minutes, width=2)
seconds_format = '{0:0{width}}'.format(seconds, width=2)
print(f'Your time: {hours_format}:{minutes_format}:{seconds_format}')
