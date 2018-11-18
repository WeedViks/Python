def sign():
    """Атомный номер (заряд ядра) - Z."""
    pass
help(sign)


Z = int(input('Введите значение Z: '))
if Z==3:
    print('Li (литий)',Z)
elif Z==17:
    print('Cl (хлор)',Z)
elif 24<Z<26:
    print('Mn (марганец)',Z)
elif Z==80:
    print('Hg (ртуть)',Z)
else:
    print('WTF?!')
