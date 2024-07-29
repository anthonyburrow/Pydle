from numpy import exp

from .....util.structures.Tool import Tool


class Log:

    def __init__(
        self,
        name: str,
        XP: float,
        level: int,
        ticks_per_fire: int,
        characteristic_level: int,
        log_value: float,
        n_per_gather: int = 1,
        min_prob_factor: float = 0.1,
        growth_rate: float = 0.15
    ):
        self.name: str = name
        self.XP: float = XP
        self.level: int = level
        self.n_per_gather: int = n_per_gather
        self.ticks_per_fire: int = ticks_per_fire

        # Rock quantities
        self.characteristic_level: int = characteristic_level
        self.log_value: float = log_value
        self.min_prob_factor: float = min_prob_factor
        self.growth_rate: float = growth_rate

    def prob_success(self, level: int, axe: Tool):
        L = axe.power * self.log_value
        k = self.growth_rate

        if level < self.level:
            return 0.

        prob = L / (1. + exp(-k * (level - self.characteristic_level)))

        min_prob = self.min_prob_factor * self.log_value
        if prob < min_prob:
            prob = min_prob

        if axe.level < self.level:
            prob *= 0.5

        return prob


logs = {
    'logs': Log(
        name='logs',
        XP=12.5,
        level=1,
        ticks_per_fire=30,
        characteristic_level=10,
        log_value=1.00,
    ),
    'oak': Log(
        name='oak logs',
        XP=22.5,
        level=10,
        ticks_per_fire=30,
        characteristic_level=20,
        log_value=0.83,
    ),
    'willow': Log(
        name='willow logs',
        XP=35.,
        level=15,
        ticks_per_fire=30,
        characteristic_level=30,
        log_value=0.69,
    ),
    'teak': Log(
        name='teak logs',
        XP=50.,
        level=20,
        ticks_per_fire=30,
        characteristic_level=40,
        log_value=0.56,
    ),
    'maple': Log(
        name='maple logs',
        XP=65.,
        level=30,
        ticks_per_fire=30,
        characteristic_level=50,
        log_value=0.46,
    ),
    'acadia': Log(
        name='acadia logs',
        XP=85.,
        level=40,
        ticks_per_fire=30,
        characteristic_level=60,
        log_value=0.37,
    ),
    'mahogany': Log(
        name='mahogany logs',
        XP=125.,
        level=60,
        ticks_per_fire=30,
        characteristic_level=70,
        log_value=0.29,
    ),
    'yew': Log(
        name='yew logs',
        XP=175.,
        level=70,
        ticks_per_fire=30,
        characteristic_level=80,
        log_value=0.22,
    ),
    'magic': Log(
        name='magic logs',
        XP=240.,
        level=80,
        ticks_per_fire=30,
        characteristic_level=90,
        log_value=0.16,
    ),
    'elder': Log(
        name='elder logs',
        XP=350.,
        level=90,
        ticks_per_fire=30,
        characteristic_level=100,
        log_value=0.11,
    ),

}
