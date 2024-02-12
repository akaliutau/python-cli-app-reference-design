import random
from abc import ABC, abstractmethod

from core.model import User


class Generator(ABC):

    @abstractmethod
    def generate(self) -> User:
        pass


class SimpleGenerator(Generator):

    first_names: list = ['Alice', 'Beatrice', 'Bob']
    last_names = ['Brown', 'White', 'Bloom']
    min_age = 20
    max_age = 90

    def __init__(self):
        self.counter = 0

    def generate(self) -> User:
        self.counter += 1
        return User(
            firstname=self.first_names[random.randint(0, 2)],
            lastname=self.last_names[random.randint(0, 2)],
            age=random.randint(self.min_age, self.max_age)
        )
