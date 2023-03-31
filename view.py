from os import system
from msvcrt import getwch
import time

from model import TelephoneContact


def list_contacts(contacts):
    table = [['ФАМИЛИЯ', 'ИМЯ', 'ОТЧЕСТВО', 'НОМЕР ТЕЛЕФОНА']]
    for c in contacts:
        contact = [c.last_name, c.first_name, c.patronymic, c.num_tel]
        table.append(contact)
    for ind, item in enumerate(table):
        if ind == 0:
            ind = '№'
        print(ind, '\t', *map(lambda x: str(x) + ' ' * (20 - len(x)), item))


def show_menu(actions):
    time.sleep(1)
    system('CLS')
    print('Выберите операцию', actions)

    n = int(getwch())
    if n in list(actions):
        system('CLS')
        return int(n)
    else:
        system('CLS')
        print('Введите из предложенных вариантов')
