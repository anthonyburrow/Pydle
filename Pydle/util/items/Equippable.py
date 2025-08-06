from .Item import Item
from ..colors import color, color_theme
from ..structures.Stats import Stats
from ..structures.Equipment import EquipmentSlot


class Equippable(Item):

    def __init__(
        self,
        item_id: str,
        name: str,
        equipment_slot: EquipmentSlot,
        tier: int,
        stats: dict = None,
    ):
        super().__init__(item_id, name)

        self.equipment_slot: EquipmentSlot = equipment_slot
        self.tier: int = tier
        self.stats = Stats(stats)

    def __str__(self):
        return color(self.name.capitalize(), color_theme['equipment'])
