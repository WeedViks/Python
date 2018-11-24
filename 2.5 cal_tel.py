def cal_tel(city,t):
    if city == 343:
        return t * 15
    if city == 381:
        return t * 18
    if city == 473:
        return t * 13
    if city == 485:
        return t * 11
    return('Код города не существует! 0')


city = int(input('Введите код города: '))
t = int(input('Введите время разговора: '))

print('Стоимость разговора составит: ', cal_tel(city, t), 'руб.')
