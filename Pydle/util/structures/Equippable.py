from ..colors import color, color_theme
from .Stats import Stats


class Equippable:

    def __init__(
        self,
        name: str,
        tier: int,
        stats: Stats = None,
    ):
        self.name: str = name
        self.tier: int = tier

        self.stats = stats
        if stats is None:
            self.stats = Stats()

    def __str__(self):
        return color(self.name.capitalize(), color_theme['equipment'])


class Weapon(Equippable):

    def __init__(self, attack_speed: int = 3, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.attack_speed = attack_speed


class Armor(Equippable):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
