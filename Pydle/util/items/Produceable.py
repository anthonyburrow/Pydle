from ...util.colors import color, color_theme
from .Item import Item


class Produceable(Item):
    def __init__(
        self,
        item_id: str,
        name: str,
        xp: float,
        level: int,
        ticks_per_action: int,
        items_required: dict,
        n_per_produce: int = 1,
    ):
        super().__init__(item_id, name)

        self.xp: float = xp
        self.level: int = level
        self.ticks_per_action: int = ticks_per_action
        self.items_required: dict = items_required
        self.n_per_produce: int = n_per_produce

    def __str__(self):
        return color(self.name.title(), color_theme['skill_artisan'])
