from numpy import exp

from ...util.structures.Tool import Tool
from ...util.colors import color, color_theme


class Gatherable:

    def __init__(
        self,
        name: str,
        XP: float,
        level: int,
        gather_value: float,
        n_per_gather: int = 1,
        characteristic_level: int = None,
        min_prob_factor: float = 0.1,
        growth_rate: float = 0.15
    ):
        self.name: str = name
        self.XP: float = XP
        self.level: int = level
        self.n_per_gather: int = n_per_gather

        # Rate quantities
        self.gather_value: float = gather_value
        self.characteristic_level: int = characteristic_level
        self.min_prob_factor: float = min_prob_factor
        self.growth_rate: float = growth_rate

    def prob_success(self, level: int, tool: Tool):
        L = tool.power * self.gather_value
        k = self.growth_rate

        if level < self.level:
            return 0.

        if self.characteristic_level is None:
            char_level = self.level + 10
        else:
            char_level = self.characteristic_level
        prob = L / (1. + exp(-k * (level - char_level)))

        min_prob = self.min_prob_factor * self.gather_value
        if prob < min_prob:
            prob = min_prob

        if tool.level < self.level:
            prob *= 0.5

        return prob

    def __str__(self):
        text: str = f'{self.name}'
        return color(text, color_theme['skill_gathering'])
