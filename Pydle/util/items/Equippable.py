from .Item import Item
from .Quality import Quality
from ..colors import color, color_theme
from ..player.EquipmentSlot import EquipmentSlot
from ..player.Stats import Stats


class Equippable(Item):

    def __init__(
        self,
        item_id: str,
        name: str,
        equipment_slot: EquipmentSlot,
        tier: int,
        stats: dict = None,
        supported_qualities: list[Quality] = None
    ):
        super().__init__(item_id, name)

        self.equipment_slot: EquipmentSlot = equipment_slot
        self.tier: int = tier
        self.stats = Stats(stats)
        self.supported_qualities: list[Quality] = \
            supported_qualities or list(Quality)

    def __str__(self):
        return color(self.name.title(), color_theme['equipment'])
