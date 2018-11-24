def num_to_name(n_atom):
    """Определение названия элемента по атомному номеру (Z)"""

    if n_atom == 3:
        return 'Li (литий)'
    if n_atom == 17:
        return 'Cl (хлор)'
    if n_atom == 25:
        return 'Mn (марганец)'
    if n_atom == 80:
        return 'Hg (ртуть)'
    return 'WTF?!'

    
n_atom = int(input('Введи атомный номер элемента: '))
print('Номер', n_atom, '-', num_to_name(n_atom))
