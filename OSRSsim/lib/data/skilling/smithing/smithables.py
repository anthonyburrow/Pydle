
class Smithable:

    def __init__(
        self,
        name: str,
        XP: float,
        level: int,
        ticks_per_action: int,
        items_required: dict,
    ):
        self.name: str = name
        self.XP: float = XP
        self.level: int = level
        self.ticks_per_action: int = ticks_per_action
        self.items_required: dict = items_required


smithables = {
    'copper gauntlets': Smithable(
        name='copper gauntlets',
        XP=15.,
        level=1,
        ticks_per_action=6,
        items_required={
            'copper bar': 1,
        },
    )
}
