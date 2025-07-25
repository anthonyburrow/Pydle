from ...util.colors import color, color_theme


class Produceable:

    def __init__(
        self,
        name: str,
        xp: float,
        level: int,
        ticks_per_action: int,
        items_required: dict,
    ):
        self.name: str = name
        self.xp: float = xp
        self.level: int = level
        self.ticks_per_action: int = ticks_per_action
        self.items_required: dict = items_required

    def __str__(self):
        text: str = f'{self.name}'
        return color(text, color_theme['skill_artisan'])
