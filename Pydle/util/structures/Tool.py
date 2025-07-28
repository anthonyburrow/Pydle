from ..colors import color, color_theme


class Tool:

    def __init__(
        self,
        name: str,
        level: int,
        power: float = None,
        ticks_per_use: int = 3,
    ):
        self.name: str = name
        self.level: int = level

        self.power: float = self._default_power() if power is None else power
        self.ticks_per_use: int = ticks_per_use

    def _default_power(self) -> float:
        return 0.5 + float(self.level) * 0.5 * 0.01

    def __str__(self):
        return color(self.name.capitalize(), color_theme['tools'])
