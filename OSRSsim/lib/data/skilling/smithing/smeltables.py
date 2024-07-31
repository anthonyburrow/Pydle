
class Smeltable:

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


smeltables = {
    'copper': Smeltable(
        name='copper bar',
        XP=6.,
        level=1,
        ticks_per_action=3,
        items_required={
            'copper ore': 1,
        },
    )
}
