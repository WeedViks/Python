def num(x):
    """Определение четности введенного числа"""
 
    if(x>=0 and x%2==0):
        return('Четное')
    elif(x<0):
        return('Число МЕНЬШЕ 0!')
    else:
        return('Нечетное')

print(num(int(input('Введите число: '))))
