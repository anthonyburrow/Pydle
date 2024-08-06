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
