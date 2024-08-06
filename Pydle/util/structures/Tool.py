from ..colors import color, color_theme


class Tool:

    def __init__(
        self,
        name: str,
        level: int,
        power: float,
        ticks_per_use: int,
    ):
        self.name: str = name

        # Use properties
        self.level: int = level
        self.power: int = power
        self.ticks_per_use: int = ticks_per_use

    def __str__(self):
        return color(self.name.capitalize(), color_theme['tools'])
