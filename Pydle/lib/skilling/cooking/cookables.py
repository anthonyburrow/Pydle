from numpy import exp


class Cookable:

    def __init__(
        self,
        name: str,
        items_required: dict,
        XP: float,
        level: int,
        ticks_per_action: int,
        characteristic_level: int,
        food_value: float,
        min_prob_factor: float = 0.1,
        growth_rate: float = 0.15
    ):
        self.name: str = name
        self.items_required: dict = items_required
        self.XP: float = XP
        self.level: int = level
        self.ticks_per_action: int = ticks_per_action

        # Burning quantities
        self.characteristic_level: int = characteristic_level
        self.food_value: float = food_value
        self.min_prob_factor: float = min_prob_factor
        self.growth_rate: float = growth_rate

    def prob_success(self, level: int):
        L = self.food_value
        k = self.growth_rate

        if level < self.level:
            return 0.

        prob = L / (1. + exp(-k * (level - self.characteristic_level)))

        min_prob = self.min_prob_factor * self.food_value
        if prob < min_prob:
            prob = min_prob

        return prob


cookables = {
    # Fish
    'shrimp': Cookable(
        name='shrimp',
        items_required={'raw shrimp': 1},
        XP=12.5,
        level=1,
        ticks_per_action=3,
        characteristic_level=10,
        food_value=1.00,
    ),
    'herring': Cookable(
        name='herring',
        items_required={'raw herring': 1},
        XP=22.5,
        level=10,
        ticks_per_action=3,
        characteristic_level=20,
        food_value=0.83,
    ),
    'bass': Cookable(
        name='bass',
        items_required={'raw bass': 1},
        XP=35.,
        level=15,
        ticks_per_action=3,
        characteristic_level=30,
        food_value=0.69,
    ),
    'trout': Cookable(
        name='trout',
        items_required={'raw trout': 1},
        XP=50.,
        level=20,
        ticks_per_action=3,
        characteristic_level=40,
        food_value=0.56,
    ),
    'salmon': Cookable(
        name='salmon',
        items_required={'raw salmon': 1},
        XP=65.,
        level=30,
        ticks_per_action=3,
        characteristic_level=50,
        food_value=0.46,
    ),
    'lobster': Cookable(
        name='lobster',
        items_required={'raw lobster': 1},
        XP=85.,
        level=40,
        ticks_per_action=3,
        characteristic_level=60,
        food_value=0.37,
    ),
    'swordfish': Cookable(
        name='swordfish',
        items_required={'raw swordfish': 1},
        XP=125.,
        level=60,
        ticks_per_action=3,
        characteristic_level=70,
        food_value=0.29,
    ),
    'shark': Cookable(
        name='shark',
        items_required={'raw shark': 1},
        XP=175.,
        level=70,
        ticks_per_action=3,
        characteristic_level=80,
        food_value=0.22,
    ),
    'anglerfish': Cookable(
        name='anglerfish',
        items_required={'raw anglerfish': 1},
        XP=240.,
        level=80,
        ticks_per_action=3,
        characteristic_level=90,
        food_value=0.16,
    ),
    'whale': Cookable(
        name='whale',
        items_required={'raw whale': 1},
        XP=350.,
        level=90,
        ticks_per_action=3,
        characteristic_level=100,
        food_value=0.11,
    ),

}
