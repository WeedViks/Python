def full_price_film(cinema,time,num_tick):
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


def discount_price_film(day,num_tick):
    if day == 'сегодня':
        if num_tick >= 20:
            return (def full_price_film(cinema,time,num_tick)) * 0.8
        if num_tick < 20:
            return (def full_price_film(cinema,time,num_tick))
    elif day == 'завтра':
        if num_tick > = 20:
            return (def full_price_film(cinema,time,num_tick)) * 0.75
        if num_tick < 20:
            return (def full_price_film(cinema,time,num_tick))
    return ('Ошибка ввода!!')


cinema = input('Выберите фильм: ')
time = int(input('Выберите время: '))
num_tick = int(input('Выберите кол-во билетов: '))
day = input('Выберите день: ')

print('Вы выбрали:\nФильм - ',cinema,'\nВремя сеанса - ',time,'\nКол-во билетов - ',num_tick,'\nДень - ',day)
print('Стоимость за ',num_tick,'билетов - ',full_price_film(cinema,time,num_tick),'руб.')
