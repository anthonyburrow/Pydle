from .Bank import Bank


class Player:

    def __init__(self):
        self.name = 'masamune'

        # Will probably change to a bank database
        self._bank = Bank()

        self._status = 'idle'

    def give(self, *args, **kwargs):
        self._bank.add(*args, **kwargs)

    def has(self, *args, **kwargs) -> bool:
        return self._bank.contains(*args, **kwargs)

    @property
    def is_busy(self) -> bool:
        return self._status == 'activity'

    # @property
    # def bank(self) -> Bank:
    #     return self._bank

    def __str__(self):
        return f'{self.name}'
