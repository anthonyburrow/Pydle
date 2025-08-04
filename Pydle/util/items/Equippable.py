from .Item import Item
from ..colors import color, color_theme
from ..structures.Stats import Stats


class Equippable(Item):

    def __init__(
        self,
        item_id: str,
        name: str,
        tier: int,
        stats: dict = None,
    ):
        super().__init__(item_id, name)

        self.tier: int = tier
        self.stats = Stats(stats)

    def __str__(self):
        return color(self.name.capitalize(), color_theme['equipment'])
