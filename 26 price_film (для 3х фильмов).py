def price_film_1(cinema,time,num_tick):
    if cinema == 'Пятница':
        if time == 12:
            return 250 * num_tick
        if time == 16:
            return 350 * num_tick
        if time == 20:
            return 450 * num_tick
    elif cinema == 'Чемпионы':
        if time == 10:
            return 250 * num_tick
        if time == 13:
            return 350 * num_tick
        if time == 16:
            return 350 * num_tick
    elif cinema == 'Пернатая банда':
        if time == 10:
            return 350 * num_tick
        if time == 14:
            return 450 * num_tick
        if time == 18:
            return 450 * num_tick
    return ('Ошибка ввода!')


cinema = input('Выберите фильм: ')
time = int(input('Выберите время: '))
num_tick = int(input('Выберите кол-во билетов: '))

print('Вы выбрали:\nФильм - ',cinema,'\nВремя сеанса - ',time,'\nКол-во билетов - ',num_tick)
print('Полная стоимость за ',num_tick,'билетов (без скидки) - ',price_film_1(cinema,time,num_tick),'руб.')
