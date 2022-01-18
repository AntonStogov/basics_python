duration = int(input('Введите количество секунд:= '))
if duration < 60:
    print(duration % 60, 'сек') # покажет количество секунд до минуты
elif duration < 3600:
    print(duration // 60 % 60, 'мин', duration % 60, 'сек') # покажет минуты и секунды до часа
elif duration < 86400:
    print(duration // 3600 % 24, 'час', duration // 60 % 60, 'мин', duration % 60, 'сек') # покажет секунды, минуты, часы до суток
else:
    print(duration // 86400, 'дн', duration // 3600 % 24, 'час', duration // 60 % 60, 'мин', duration % 60, 'сек') # задание со звездочкой

    # для проверки введите 400153 ответ: 4 дн 15 час 9 мин 13 сек
