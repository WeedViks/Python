def cal_tel(city):
    if city == 343: return (t*15)
    if city == 381: return (t*18)
    if city == 473: return (t*13)
    if city == 485: return (t*11)

city = int(input('Введите код города: '))
t = int(input('Введите время разговора: '))

print('Стоимость разговора составит: ', cal_tel(city), 'руб.')
