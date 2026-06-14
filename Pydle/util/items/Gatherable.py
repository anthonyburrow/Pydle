from numpy import exp

from ..colors import color, color_theme
from ..ticks import Ticks
from .Item import Item
from .Tool import Tool


class Gatherable(Item):
    def __init__(
        self,
        item_id: str,
        name: str,
        xp: float,
        level: int,
        gather_value: float | None = None,
        n_per_gather: int = 1,
        characteristic_level: int | None = None,
        min_prob_factor: float = 0.1,
        growth_rate: float = 0.15,
    ):
        super().__init__(item_id, name)

        self.xp: float = xp
        self.level: int = level
        self.n_per_gather: int = n_per_gather

        # Rate quantities
        self.gather_value: float = gather_value or self._default_gather_value()
        self.characteristic_level: int = (
            characteristic_level or self._default_characteristic_level()
        )
        self.min_prob_factor: float = min_prob_factor
        self.growth_rate: float = growth_rate

    def prob_success(self, level: int, tool: Tool):
        L = tool.power * self.gather_value
        k = self.growth_rate

        if level < self.level:
            return 0.0

        prob = L / (1.0 + exp(-k * (level - self.characteristic_level)))

        min_prob = self.min_prob_factor * self.gather_value
        if prob < min_prob:
            prob = min_prob

        if tool.level < self.level:
            prob *= 0.5

        return prob

    def _default_gather_value(self) -> float:
        # gather_value = xp_rate * ticks_per_gather / (n_ticks * tool_power * self.xp)
        n_ticks: float = 3_600.0 / Ticks()
        tool_power: float = 0.5 + float(self.level) * 0.5 * 0.01
        xp_rate: float = float(self.level) * 800.0 + 5_000.0

        gather_value: float = xp_rate * 3.0 / (n_ticks * tool_power * self.xp)
        gather_value = min(1.0, gather_value)

        return gather_value

    def _default_characteristic_level(self) -> int:
        return self.level + 10

    def __str__(self):
        return color(self.name.title(), color_theme['skill_gathering'])
