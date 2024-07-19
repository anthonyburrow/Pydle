from numpy import exp


class Ore:

    def __init__(
        self,
        name: str,
        XP: float,
        level: int,
        characteristic_level: int,
        ore_value: float,
        n_per_gather: int = 1,
        min_prob_factor: float = 0.1,
        growth_rate: float = 0.15
    ):
        self.name: str = name
        self.XP: float = XP
        self.level: int = level
        self.n_per_gather: int = n_per_gather

        # Rock quantities
        self.characteristic_level: int = characteristic_level
        self.ore_value: float = ore_value
        self.min_prob_factor: float = min_prob_factor
        self.growth_rate: float = growth_rate

    def prob_success(self, level: int, pickaxe_power: float,
                     pickaxe_level: int):
        L = pickaxe_power * self.ore_value
        k = self.growth_rate

        if level < self.level:
            return 0.

        prob = L / (1. + exp(-k * (level - self.characteristic_level)))

        min_prob = self.min_prob_factor * self.ore_value
        if prob < min_prob:
            prob = min_prob

        if pickaxe_level < self.level:
            prob *= 0.5

        return prob


ores = {
    'copper': Ore(
        name='copper ore',
        XP=12.5,
        level=1,
        characteristic_level=10,
        ore_value=1.00,
    ),
    'iron': Ore(
        name='iron ore',
        XP=22.5,
        level=10,
        characteristic_level=20,
        ore_value=0.83,
    ),
    'coal': Ore(
        name='coal',
        XP=35.,
        level=15,
        characteristic_level=30,
        ore_value=0.69,
    ),
    'mithril': Ore(
        name='mithril ore',
        XP=50.,
        level=20,
        characteristic_level=40,
        ore_value=0.56,
    ),
    'adamant': Ore(
        name='adamantite ore',
        XP=65.,
        level=30,
        characteristic_level=50,
        ore_value=0.46,
    ),
    'rune': Ore(
        name='runite ore',
        XP=85.,
        level=40,
        characteristic_level=60,
        ore_value=0.37,
    ),
    'orikalkum': Ore(
        name='orikalkum ore',
        XP=125.,
        level=60,
        characteristic_level=70,
        ore_value=0.29,
    ),
    'necronium': Ore(
        name='necronium ore',
        XP=175.,
        level=70,
        characteristic_level=80,
        ore_value=0.22,
    ),
    'bane': Ore(
        name='banite ore',
        XP=240.,
        level=80,
        characteristic_level=90,
        ore_value=0.16,
    ),
    'elder': Ore(
        name='elder ore',
        XP=350.,
        level=90,
        characteristic_level=100,
        ore_value=0.11,
    ),

}
