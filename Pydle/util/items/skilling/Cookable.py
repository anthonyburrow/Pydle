from numpy import exp

from ..Produceable import Produceable


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
