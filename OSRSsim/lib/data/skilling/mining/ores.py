class Ore:

    def __init__(self, name: str, XP: int, prob_success: float,
                 n_per_ore: int = 1):
        self.name = name
        self.XP = XP
        self.prob_success = prob_success
        self.n_per_ore = n_per_ore


ores = {
    'iron': Ore(
        name='Iron ore',
        XP=35,
        prob_success=0.5,
    ),
}
