from typing import Dict


class User(object):
    """Model class for User
    """

    def __init__(self, firstname: str, lastname: str, age: int):
        self._firstname = firstname
        self._lastname = lastname
        self._age = age

    @property
    def firstname(self) -> str:
        return self._firstname

    @firstname.setter
    def firstname(self, name: str):
        self._firstname = name

    @property
    def lastname(self) -> str:
        return self._lastname

    @lastname.setter
    def lastname(self, name: str):
        self._lastname = name

    @property
    def age(self) -> int:
        return self._age

    @age.setter
    def age(self, age: str):
        self._age = age

    def to_json(self) -> Dict[str, any]:
        return {
            'firstname': self._firstname,
            'lastname': self._lastname,
            'age': self._age
        }
