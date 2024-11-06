import re

from field import Field


class Phone(Field):
    PHONE_REGEXP = re.compile(r"^\d{10}$")

    def __init__(self, value):
        if self._is_valid_value(value):
            super().__init__(value)
        else:
            raise ValueError("The phone number must consist of only 10 digits")

    def _is_valid_value(self, value):
        return Phone.PHONE_REGEXP.match(value) is not None


if __name__ == "__main__":
    for value in ["123", "abc", "0123456789"]:
        try:
            phone = Phone(value)
            print(f"Phone number: {phone}")
        except Exception as e:
            print(f"Value: {value}, error: {e}")
