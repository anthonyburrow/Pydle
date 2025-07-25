
class Produceable:

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
