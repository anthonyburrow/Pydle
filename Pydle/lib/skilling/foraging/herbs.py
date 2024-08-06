from numpy import exp

from ....util.structures.Tool import Tool


class Herb:

    def __init__(
        self,
        # Herb properties
        name_grimy: str,
        name_clean: str,
        level: int,
        n_per_gather: int,
        # XP
        XP: float,
        XP_clean: float,
        # Gathering quantities
        characteristic_level: int,
        herb_value: float,
        min_prob_factor: float = 0.1,
        growth_rate: float = 0.15
    ):
        # Herb properties
        self.name_grimy: str = name_grimy
        self.name_clean: str = name_clean
        self.level: int = level
        self.n_per_gather: int = n_per_gather

        # XP
        self.XP: float = XP
        self.XP_clean: float = XP_clean

        # Gathering quantities
        self.characteristic_level: int = characteristic_level
        self.herb_value: float = herb_value
        self.min_prob_factor: float = min_prob_factor
        self.growth_rate: float = growth_rate

    def prob_success(self, level: int, secateurs: Tool):
        L = secateurs.power * self.herb_value
        k = self.growth_rate

        if level < self.level:
            return 0.

        prob = L / (1. + exp(-k * (level - self.characteristic_level)))

        min_prob = self.min_prob_factor * self.herb_value
        if prob < min_prob:
            prob = min_prob

        if secateurs.level < self.level:
            prob *= 0.5

        return prob


herbs = {
    'guam': Herb(
        name_grimy='grimy guam',
        name_clean='clean guam',
        level=1,
        n_per_gather=1,
        XP=12.5,
        XP_clean=1.,
        characteristic_level=10,
        herb_value=1.00,
    ),
    'marrentill': Herb(
        name_grimy='grimy marrentill',
        name_clean='clean marrentill',
        level=10,
        n_per_gather=1,
        XP=22.5,
        XP_clean=2.,
        characteristic_level=20,
        herb_value=0.83,
    ),
    'harralander': Herb(
        name_grimy='grimy harralander',
        name_clean='clean harralander',
        level=15,
        n_per_gather=1,
        XP=35.,
        XP_clean=3.5,
        characteristic_level=30,
        herb_value=0.69,
    ),
    'ranarr': Herb(
        name_grimy='grimy ranarr',
        name_clean='clean ranarr',
        level=20,
        n_per_gather=1,
        XP=50.,
        XP_clean=5.,
        characteristic_level=40,
        herb_value=0.56,
    ),
    'toadflax': Herb(
        name_grimy='grimy toadflax',
        name_clean='clean toadflax',
        level=30,
        n_per_gather=1,
        XP=65.,
        XP_clean=6.5,
        characteristic_level=50,
        herb_value=0.46,
    ),
    'irit': Herb(
        name_grimy='grimy irit',
        name_clean='clean irit',
        level=40,
        n_per_gather=1,
        XP=85.,
        XP_clean=8.5,
        characteristic_level=60,
        herb_value=0.37,
    ),
    'kwuarm': Herb(
        name_grimy='grimy avantoe',
        name_clean='clean avantoe',
        level=60,
        n_per_gather=1,
        XP=125.,
        XP_clean=12.5,
        characteristic_level=70,
        herb_value=0.29,
    ),
    'snapdragon': Herb(
        name_grimy='grimy snapdragon',
        name_clean='clean snapdragon',
        level=70,
        n_per_gather=1,
        XP=175.,
        XP_clean=17.5,
        characteristic_level=80,
        herb_value=0.22,
    ),
    'torstol': Herb(
        name_grimy='grimy torstol',
        name_clean='clean torstol',
        level=80,
        n_per_gather=1,
        XP=240.,
        XP_clean=24.,
        characteristic_level=90,
        herb_value=0.16,
    ),
    'fellstalk': Herb(
        name_grimy='grimy fellstalk',
        name_clean='clean fellstalk',
        level=90,
        n_per_gather=1,
        XP=350.,
        XP_clean=35.,
        characteristic_level=100,
        herb_value=0.11,
    ),

}
