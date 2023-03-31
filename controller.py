from os import system
import time

from model import TelephoneContact
from repository import TelephoneRepository
import view


def run():
    actions = {
        1: 'Создать контакт',
        2: 'Прочитать книгу',
        3: 'Изменить контакт',
        4: 'Удалить контакт',
        5: 'Выгрузить в файл',
        6: 'Выход'
    }
    repository = TelephoneRepository()
    repository.import_contacts()

    while True:
        n = view.show_menu(actions)
        if n == 1:
            contact = request_contact_data(None)
            repository.save_contact(contact)
            print("\nКонтакт сохранен\n")
        if n == 2:
            contacts = repository.get_contacts()
            view.list_contacts(contacts)
        if n == 3:
            print("\nВведите номер контакта для изменения\n")
            num_contact = input('Какой контакт изменить? Введите телефон: ')
            if num_contact.isdigit():
                contact = request_contact_data(num_contact)
                repository.update_contact(contact)
                print('\nКонтакт удален')
            else:
                print("Неверно введен номер контакта")
        if n == 4:
            print("\nВведите номер контакта для удаления\n")
            num_contact = input('Какой номер контакта удалить?: ')
            if num_contact.isdigit():
                repository.delete_contact(int(num_contact))
                print('\nКонтакт удален')
            else:
                print("Неверно введен номер контакта")
        if n == 5:
            repository.export_contacts()
            print("Данные сохранены в файл.")
        if n == 6:
            break


def request_contact_data(num_contact):
    print("\nВведите имя для контакта\n")
    first_name = input()
    system('CLS')
    time.sleep(1)
    print("\nВведите фамилию для контакта\n")
    last_name = input()
    system('CLS')
    time.sleep(1)
    print("\nВведите отчество для контакта\n")
    patronymic = input()
    system('CLS')
    time.sleep(1)
    if num_contact is None:
        print("\nВведите телефон для контакта\n")
        num_contact = input()
        system('CLS')
    return TelephoneContact(first_name, last_name, patronymic, num_contact)
