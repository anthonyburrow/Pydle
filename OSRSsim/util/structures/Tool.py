from ..colors import color, COLOR_TOOLS


class Tool:

    def __init__(
        self,
        name: str,
        level: int,
        power: float,
        ticks_per_use: int,
    ):
        self.name = name

        # Use properties
        self.level: int = level
        self.power: int = power
        self.ticks_per_use: int = ticks_per_use

    def __str__(self):
        return color(self.name.capitalize(), COLOR_TOOLS)
