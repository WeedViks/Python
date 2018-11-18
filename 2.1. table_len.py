value = input('Введите значение Z: ')
if len(value) > 0:
    Z = int(value)
    if Z==3:
        print(Z,'Li (литий)')
    elif Z==17:
        print('Cl (хлор)',Z)
    elif 24<Z<26:
        print('Mn (марганец)',Z)
    elif Z==80:
        print('Hg (ртуть)',Z)
    else:
        print('WTF?!')
else:
    print('Введите значение Z, ЁП!!!')
