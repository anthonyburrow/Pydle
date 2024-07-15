from numpy import exp


class Ore:

    def __init__(
        self,
        name: str,
        XP: float,
        level: int,
        characteristic_level: int,
        ore_value: float,
        n_per_ore: int = 1,
        min_prob_factor: float = 0.1,
        growth_rate: float = 0.15
    ):
        self.name: str = name
        self.XP: float = XP
        self.level: int = level
        self.n_per_ore: int = n_per_ore

        # Rock quantities
        self.characteristic_level: int = characteristic_level
        self.ore_value: float = ore_value
        self.min_prob_factor: float = min_prob_factor
        self.growth_rate: float = growth_rate

    def prob_success(self, level: int, pickaxe_power: float):
        L = pickaxe_power * self.ore_value
        k = self.growth_rate

        if level < self.level:
            return 0.

        prob = L / (1. + exp(-k * (level - self.characteristic_level)))

        min_prob = self.min_prob_factor * self.ore_value
        if prob < min_prob:
            return min_prob

        return prob


ores = {
    'copper': Ore(
        name='Copper ore',
        XP=12.5,
        level=1,
        characteristic_level=10,
        ore_value=0.95,
    ),
    'iron': Ore(
        name='Iron ore',
        XP=25.,
        level=10,
        characteristic_level=25,
        ore_value=0.85,
    ),
    'coal': Ore(
        name='Coal',
        XP=35,
        level=15,
        characteristic_level=30,
        ore_value=0.75,
    ),
    'mithril': Ore(
        name='Mithril ore',
        XP=55.,
        level=20,
        characteristic_level=40,
        ore_value=0.65,
    ),
    'adamant': Ore(
        name='Adamantite ore',
        XP=70.,
        level=30,
        characteristic_level=50,
        ore_value=0.55,
    ),
    'rune': Ore(
        name='Runite ore',
        XP=95.,
        level=40,
        characteristic_level=60,
        ore_value=0.40,
    ),
    'orikalkum': Ore(
        name='Orikalkum ore',
        XP=150.,
        level=60,
        characteristic_level=70,
        ore_value=0.25,
    ),
    'necronium': Ore(
        name='Necronium ore',
        XP=185.,
        level=70,
        characteristic_level=80,
        ore_value=0.20,
    ),
    'bane': Ore(
        name='Banite ore',
        XP=245.,
        level=80,
        characteristic_level=90,
        ore_value=0.15,
    ),
    'elder': Ore(
        name='Elder ore',
        XP=350.,
        level=90,
        characteristic_level=100,
        ore_value=0.10,
    ),

}
