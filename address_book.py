from collections import UserDict

from record import Record


class AddressBook(UserDict[str, Record]):

    def find(self, name: str) -> Record | None:
        result = [record for record in self.data if record == name]
        if result:
            record_name = result[0]
            return self.data[record_name]
        else:
            return None

    def add_record(self, record: Record):
        if self.find(record.name.value) is not None:
            raise KeyError(
                f"Record with name '{record.name.value}' already exists in the addressbook"
            )

        self.data[record.name.value] = record

    def delete(self, name: str):
        if name in self.data:
            del self.data[name]


if __name__ == "__main__":
    try:
        # Створення нової адресної книги
        book = AddressBook()

        # Створення запису для John
        john_record = Record("John")
        john_record.add_phone("1234567890")
        john_record.add_phone("5555555555")

        # Додавання запису John до адресної книги
        book.add_record(john_record)
    except Exception as e:
        print(e)
