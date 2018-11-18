def my_max(x,y):
    """Определение MAX из двух введенных чисел"""
    if x>y:
        return x
    else:
        return y

x=int(input('Введите первое число: '))
y=int(input('Введите второе число: '))

print('MAX число: ', my_max(x,y))
