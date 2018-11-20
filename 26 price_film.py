def price_film_1(cinema,t,num_tick):
    if cinema == 'Пятница' and time == 12:
        return 250 * num_tick
    elif cinema == 'Пятница' and time == 16:
        return 350 * num_tick
    elif cinema == 'Пятница' and time == 20:
        return 450 * num_tick
    return ('Ошибка ввода!')


cinema = int(input('Выберите фильм: '))
time = int(input('Выберите время: '))
num_tick = int(input('Выберите кол-во билетов: '))

print('Полная стоимость билетов за ',num_tick,'билетов, составит - ',price_film_1(cinema,t,num_tick),'руб.')
