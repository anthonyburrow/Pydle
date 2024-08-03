

class Craftable:

    def __init__(
        self,
        name: str,
        level: int,
        XP: float,
        items_required: dict,
        ticks_per_action: int,
    ):
        self.name: str = name
        self.level: int = level
        self.XP: float = XP
        self.items_required: dict = items_required
        self.ticks_per_action: int = ticks_per_action


craftables = {
    'leather': Craftable(
        name='leather',
        level=1,
        XP=6.,
        items_required={
            'raw hide': 1,
        },
        ticks_per_action=2,
    ),
    'leather gloves': Craftable(
        name='leather gloves',
        level=1,
        XP=15.,
        items_required={
            'leather': 1,
        },
        ticks_per_action=5,
    ),
}
