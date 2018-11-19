def num(x):
    
    """Определение четности введенного числа"""
 
    if x % 2 == 0:
        return('Четное')
    else:
        return('Нечетное')


x = int(input('Введите число: '))
print(num(x))
