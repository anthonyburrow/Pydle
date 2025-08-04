from .Equippable import Equippable


class Weapon(Equippable):

    def __init__(self, attack_speed: int = 3, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.attack_speed = attack_speed
