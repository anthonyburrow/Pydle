

class Mixable:

    def __init__(
        self,
        # Herb properties
        name: str,
        n_doses: int,
        level: int,
        XP: float,
        items_required: dict,
        ticks_per_action: int,
    ):
        # Herb properties
        self.name: str = name
        self.n_doses: int = n_doses
        self.level: int = level
        self.XP: float = XP
        self.items_required: dict = items_required
        self.ticks_per_action: int = ticks_per_action


mixables = {
    'attack': Mixable(
        name='attack potion',
        n_doses=3,
        level=1,
        XP=25.,
        items_required={
            'vial': 3,
            'clean guam': 1,
            'eye of newt': 1,
        },
        ticks_per_action=5,
    ),
}
