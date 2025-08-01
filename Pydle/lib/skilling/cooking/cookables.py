from numpy import exp

from ....util.structures.Produceable import Produceable


class Cookable(Produceable):

    def __init__(
        self,
        # Burning quantities
        characteristic_level: int,
        produce_value: float,
        min_prob_factor: float = 0.1,
        growth_rate: float = 0.15,
        *args,
        **kwargs
    ):
        super().__init__(*args, **kwargs)

        # Burning quantities
        self.characteristic_level: int = characteristic_level
        self.produce_value: float = produce_value
        self.min_prob_factor: float = min_prob_factor
        self.growth_rate: float = growth_rate

    def prob_success(self, level: int):
        L = self.produce_value
        k = self.growth_rate

        if level < self.level:
            return 0.

        prob = L / (1. + exp(-k * (level - self.characteristic_level)))

        min_prob = self.min_prob_factor * self.produce_value
        if prob < min_prob:
            prob = min_prob

        return prob


COOKABLES = {
    # Fish
    'shrimp': Cookable(
        name='shrimp',
        items_required={'raw shrimp': 1},
        xp=12.5,
        level=1,
        ticks_per_action=3,
        characteristic_level=10,
        produce_value=1.00,
    ),
    'anchovy': Cookable(
        name='anchovy',
        items_required={'raw anchovy': 1},
        xp=22.5,
        level=10,
        ticks_per_action=3,
        characteristic_level=20,
        produce_value=0.83,
    ),
    'trout': Cookable(
        name='trout',
        items_required={'raw trout': 1},
        xp=35.,
        level=15,
        ticks_per_action=3,
        characteristic_level=30,
        produce_value=0.69,
    ),
    'cod': Cookable(
        name='cod',
        items_required={'raw cod': 1},
        xp=50.,
        level=20,
        ticks_per_action=3,
        characteristic_level=40,
        produce_value=0.56,
    ),
    'catfish': Cookable(
        name='catfish',
        items_required={'raw catfish': 1},
        xp=65.,
        level=30,
        ticks_per_action=3,
        characteristic_level=50,
        produce_value=0.46,
    ),
    'bass': Cookable(
        name='bass',
        items_required={'raw bass': 1},
        xp=85.,
        level=40,
        ticks_per_action=3,
        characteristic_level=60,
        produce_value=0.37,
    ),
}
