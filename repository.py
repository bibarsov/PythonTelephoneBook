import json
from model import TelephoneContact


class TelephoneRepository:

    def __init__(self):
        self.contacts: list[TelephoneContact] = list()

    def save_contact(self, contact: TelephoneContact):
        self.contacts.append(contact)

    def get_contacts(self):
        return self.contacts

    def update_contact(self, contact: TelephoneContact):
        idx = 0
        for ex_con in self.contacts:
            if ex_con.num_tel == contact.num_tel:
                self.contacts[idx] = contact
                break
            idx += 1

    def delete_contact(self, num_tel: int):
        print(num_tel)
        idx = 0
        for ex_con in self.contacts:
            if int(ex_con.num_tel) == num_tel:
                del self.contacts[idx]
                break
            idx += 1

    # considered to be in a service, not in a repository
    def import_contacts(self):
        with open('initial_data.json', 'r', encoding="utf-8") as data:
            for item in json.loads(data.read()):
                self.save_contact(TelephoneContact(
                    item['First name'],
                    item['Last name'],
                    item['Patronymic'],
                    item['Telephone']
                ))

    # considered to be in a service, not in a repository
    def export_contacts(self):
        with open('initial_data.json', 'w', encoding="utf-8") as data:
            to_dump = map(lambda x: dict(
                {"First name": x.first_name, "Last name": x.last_name, "Patronymic": x.patronymic,
                 "Telephone": x.num_tel}), self.contacts)
            json.dump(list(to_dump), data, indent=4, ensure_ascii=False)
