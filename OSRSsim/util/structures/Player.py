import pickle

from .Bank import Bank
from ..colors import color, COLOR_CHARACTER


class Player:

    def __init__(self, save_file: str):
        self.name: str = input('Character name?\n> ')
        self.save_file: str = save_file

        # Will probably change to a bank database
        self._bank: Bank = Bank()

    def give(self, *args, **kwargs):
        self._bank.add(*args, **kwargs)

    def has(self, *args, **kwargs) -> bool:
        return self._bank.contains(*args, **kwargs)

    @property
    def bank(self) -> Bank:
        return self._bank

    def save(self):
        with open(self.save_file, 'wb') as file:
            pickle.dump(self, file)

    def __str__(self):
        text: str = f'{self.name}'
        return color(text, COLOR_CHARACTER)
