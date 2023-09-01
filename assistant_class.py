from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value


class AddressBook(UserDict):
    def add_record(self, data):
        self.data[data.name.value] = data


class Record():
    def __init__(self, name: str, phone=None):
        self.name = name
        self.phones = []
        if phone:
            self.phones.append(phone)


class Name(Field):
    pass


class Phone(Field):
    pass


if __name__ == "__main__":
    name = Name('Ivan')
    phone = Phone('9877890099')
    rec = Record(name, phone)
    ab = AddressBook()
    ab.add_record(rec)

# print(ab)

# Tests:
assert isinstance(ab['Ivan'], Record)
assert isinstance(ab['Ivan'].name, Name)
assert isinstance(ab['Ivan'].phones, list)
assert isinstance(ab['Ivan'].phones[0], Phone)
assert ab['Ivan'].phones[0].value == '9877890099'
