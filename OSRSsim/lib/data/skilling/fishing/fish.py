from numpy import exp

from .....util.structures.Tool import Tool


class Fish:

    def __init__(
        self,
        # Fish properties
        name: str,
        level: int,
        n_per_gather: int,
        XP: float,
        # Gathering quantities
        characteristic_level: int,
        fish_value: float,
        min_prob_factor: float = 0.1,
        growth_rate: float = 0.15
    ):
        # Fish properties
        self.name: str = name
        self.level: int = level
        self.n_per_gather: int = n_per_gather
        self.XP: float = XP

        # Gathering quantities
        self.characteristic_level: int = characteristic_level
        self.fish_value: float = fish_value
        self.min_prob_factor: float = min_prob_factor
        self.growth_rate: float = growth_rate

    def prob_success(self, level: int, fishing_rod: Tool):
        L = fishing_rod.power * self.fish_value
        k = self.growth_rate

        if level < self.level:
            return 0.

        prob = L / (1. + exp(-k * (level - self.characteristic_level)))

        min_prob = self.min_prob_factor * self.fish_value
        if prob < min_prob:
            prob = min_prob

        if fishing_rod.level < self.level:
            prob *= 0.5

        return prob


fish = {
    'shrimp': Fish(
        name='raw shrimp',
        level=1,
        n_per_gather=1,
        XP=12.5,
        characteristic_level=10,
        fish_value=1.00,
    ),
    'herring': Fish(
        name='raw herring',
        level=10,
        n_per_gather=1,
        XP=22.5,
        characteristic_level=20,
        fish_value=0.83,
    ),
    'bass': Fish(
        name='raw bass',
        level=15,
        n_per_gather=1,
        XP=35.,
        characteristic_level=30,
        fish_value=0.69,
    ),
    'trout': Fish(
        name='raw trout',
        level=20,
        n_per_gather=1,
        XP=50.,
        characteristic_level=40,
        fish_value=0.56,
    ),
    'salmon': Fish(
        name='raw salmon',
        level=30,
        n_per_gather=1,
        XP=65.,
        characteristic_level=50,
        fish_value=0.46,
    ),
    'lobster': Fish(
        name='raw lobster',
        level=40,
        n_per_gather=1,
        XP=85.,
        characteristic_level=60,
        fish_value=0.37,
    ),
    'swordfish': Fish(
        name='raw swordfish',
        level=60,
        n_per_gather=1,
        XP=125.,
        characteristic_level=70,
        fish_value=0.29,
    ),
    'shark': Fish(
        name='raw shark',
        level=70,
        n_per_gather=1,
        XP=175.,
        characteristic_level=80,
        fish_value=0.22,
    ),
    'anglerfish': Fish(
        name='raw anglerfish',
        level=80,
        n_per_gather=1,
        XP=240.,
        characteristic_level=90,
        fish_value=0.16,
    ),
    'whale': Fish(
        name='raw whale',
        level=90,
        n_per_gather=1,
        XP=350.,
        characteristic_level=100,
        fish_value=0.11,
    ),

}
