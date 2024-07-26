from numpy import exp

from .....util.structures import Tool


class Fish:

    def __init__(
        self,
        # Fish properties
        name_raw: str,
        name_cooked: str,
        level: int,
        n_per_gather: int,
        # XP
        XP: float,
        XP_cook: float,
        # Gathering quantities
        characteristic_level: int,
        fish_value: float,
        min_prob_factor: float = 0.1,
        growth_rate: float = 0.15
    ):
        # Fish properties
        self.name_raw: str = name_raw
        self.name_cooked: str = name_cooked
        self.level: int = level
        self.n_per_gather: int = n_per_gather

        # XP
        self.XP: float = XP
        self.XP_cook: float = XP_cook

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
        name_raw='raw shrimp',
        name_cooked='shrimp',
        level=1,
        n_per_gather=1,
        XP=12.5,
        XP_cook=1.,
        characteristic_level=10,
        fish_value=1.00,
    ),
    'herring': Fish(
        name_raw='raw herring',
        name_cooked='herring',
        level=10,
        n_per_gather=1,
        XP=22.5,
        XP_cook=2.,
        characteristic_level=20,
        fish_value=0.83,
    ),
    'bass': Fish(
        name_raw='raw bass',
        name_cooked='bass',
        level=15,
        n_per_gather=1,
        XP=35.,
        XP_cook=3.5,
        characteristic_level=30,
        fish_value=0.69,
    ),
    'trout': Fish(
        name_raw='raw trout',
        name_cooked='trout',
        level=20,
        n_per_gather=1,
        XP=50.,
        XP_cook=5.,
        characteristic_level=40,
        fish_value=0.56,
    ),
    'salmon': Fish(
        name_raw='raw salmon',
        name_cooked='salmon',
        level=30,
        n_per_gather=1,
        XP=65.,
        XP_cook=6.5,
        characteristic_level=50,
        fish_value=0.46,
    ),
    'lobster': Fish(
        name_raw='raw lobster',
        name_cooked='lobster',
        level=40,
        n_per_gather=1,
        XP=85.,
        XP_cook=8.5,
        characteristic_level=60,
        fish_value=0.37,
    ),
    'swordfish': Fish(
        name_raw='raw swordfish',
        name_cooked='swordfish',
        level=60,
        n_per_gather=1,
        XP=125.,
        XP_cook=12.5,
        characteristic_level=70,
        fish_value=0.29,
    ),
    'shark': Fish(
        name_raw='raw shark',
        name_cooked='shark',
        level=70,
        n_per_gather=1,
        XP=175.,
        XP_cook=17.5,
        characteristic_level=80,
        fish_value=0.22,
    ),
    'anglerfish': Fish(
        name_raw='raw anglerfish',
        name_cooked='anglerfish',
        level=80,
        n_per_gather=1,
        XP=240.,
        XP_cook=24.,
        characteristic_level=90,
        fish_value=0.16,
    ),
    'whale': Fish(
        name_raw='raw whale',
        name_cooked='whale',
        level=90,
        n_per_gather=1,
        XP=350.,
        XP_cook=35.,
        characteristic_level=100,
        fish_value=0.11,
    ),

}
