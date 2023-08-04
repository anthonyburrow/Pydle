from .Bank import Bank


class Player:

    def __init__(self):
        self.name = 'masamune'
        # Will probably change to a bank database
        self.bank = Bank()
