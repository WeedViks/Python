def fun1(x):
    """Вычисление значения функции"""

    if -2.4 <= x <= 5.7:
        return pow(x,2)
    else:
        return 4


print(fun1(float(input('Введите число: '))))

