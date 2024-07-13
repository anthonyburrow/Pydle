import pickle

from .Bank import Bank


class Player:

    def __init__(self, save_file):
        self.name = input('Character name?\n> ')
        self.save_file = save_file

        # Will probably change to a bank database
        self._bank = Bank()

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
        return f'{self.name}'
