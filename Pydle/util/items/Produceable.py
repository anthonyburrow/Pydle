from .Item import Item
from ...util.colors import color, color_theme


class Produceable(Item):

    def __init__(
        self,
        item_id: str,
        name: str,
        xp: float,
        level: int,
        ticks_per_action: int,
        items_required: dict,
    ):
        super().__init__(item_id, name)

        self.xp: float = xp
        self.level: int = level
        self.ticks_per_action: int = ticks_per_action
        self.items_required: dict = items_required

    def __str__(self):
        text: str = f'{self.name}'
        return color(text, color_theme['skill_artisan'])
