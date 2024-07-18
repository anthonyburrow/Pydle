from numpy import exp


class Log:

    def __init__(
        self,
        name: str,
        XP: float,
        level: int,
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

        # Rock quantities
        self.characteristic_level: int = characteristic_level
        self.log_value: float = log_value
        self.min_prob_factor: float = min_prob_factor
        self.growth_rate: float = growth_rate

    def prob_success(self, level: int, axe_power: float, axe_level: int):
        L = axe_power * self.log_value
        k = self.growth_rate

        if level < self.level:
            return 0.

        prob = L / (1. + exp(-k * (level - self.characteristic_level)))

        min_prob = self.min_prob_factor * self.log_value
        if prob < min_prob:
            prob = min_prob

        if axe_level < self.level:
            prob *= 0.5

        return prob


logs = {
    'logs': Log(
        name='Logs',
        XP=12.5,
        level=1,
        characteristic_level=10,
        log_value=1.00,
    ),
    'oak': Log(
        name='Oak logs',
        XP=22.5,
        level=10,
        characteristic_level=20,
        log_value=0.83,
    ),
    'willow': Log(
        name='Willow logs',
        XP=35.,
        level=15,
        characteristic_level=30,
        log_value=0.69,
    ),
    'teak': Log(
        name='Teak logs',
        XP=50.,
        level=20,
        characteristic_level=40,
        log_value=0.56,
    ),
    'maple': Log(
        name='Maple logs',
        XP=65.,
        level=30,
        characteristic_level=50,
        log_value=0.46,
    ),
    'acadia': Log(
        name='Acadia logs',
        XP=85.,
        level=40,
        characteristic_level=60,
        log_value=0.37,
    ),
    'mahogany': Log(
        name='Mahogany logs',
        XP=125.,
        level=60,
        characteristic_level=70,
        log_value=0.29,
    ),
    'yew': Log(
        name='Yew logs',
        XP=175.,
        level=70,
        characteristic_level=80,
        log_value=0.22,
    ),
    'magic': Log(
        name='Magic logs',
        XP=240.,
        level=80,
        characteristic_level=90,
        log_value=0.16,
    ),
    'elder': Log(
        name='Elder logs',
        XP=350.,
        level=90,
        characteristic_level=100,
        log_value=0.11,
    ),

}
