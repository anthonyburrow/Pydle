from .Item import Item
from .Quality import Quality
from ..colors import color, color_theme
from ..player.ToolSlot import ToolSlot


class Tool(Item):

    def __init__(
        self,
        item_id: str,
        name: str,
        tool_slot: ToolSlot, 
        level: int,
        power: float = None,
        ticks_per_use: int = 3,
        supported_qualities: list[Quality] = None
    ):
        super().__init__(item_id, name)

        self.tool_slot: ToolSlot = tool_slot
        self.level: int = level

        self.power: float = self._default_power() if power is None else power
        self.ticks_per_use: int = ticks_per_use

        self.supported_qualities: list[Quality] = \
            supported_qualities or list(Quality)

    def _default_power(self) -> float:
        return 0.5 + float(self.level) * 0.5 * 0.01

    def __str__(self):
        return color(self.name.title(), color_theme['tools'])
