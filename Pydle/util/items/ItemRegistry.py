from .Item import Item
from ..player.BankKey import BankKey

from .Armor import Armor
from .Weapon import Weapon
from .Tool import Tool
from .skilling import (
    Collectable,
    Cookable,
    Craftable,
    Fish,
    Log,
    Mixable,
    Ore,
    Smeltable,
    Smithable,
)

from ...lib.misc_items import MISC_ITEMS
from ...lib.equipment import (
    HELMS,
    BODIES,
    LEGS,
    BOOTS,
    GLOVES,
    WEAPONS,
    OFFHANDS,
)
from ...lib.skilling.cooking import COOKABLES
from ...lib.skilling.crafting import CRAFTABLES
from ...lib.skilling.fishing import FISH, FISHING_RODS
from ...lib.skilling.foraging import COLLECTABLES, SECATEURS
from ...lib.skilling.herblore import MIXABLES
from ...lib.skilling.mining import ORES, PICKAXES
from ...lib.skilling.smithing import SMELTABLES, SMITHABLES
from ...lib.skilling.woodcutting import LOGS, AXES


class ItemRegistry(dict):
    def __init__(self):
        pass

    def register(self, item_id: str, item: Item):
        if item_id in self:
            raise ValueError(f'Duplicate item_id: {item_id}')
        self[item_id] = item

    def load_from_dict(self, item_dict: dict[str, dict], item_cls: type[Item]):
        for item_id, item_kwargs in item_dict.items():
            item = item_cls(item_id=item_id, **item_kwargs)
            self.register(f'{item_cls.__name__} {item_id}', item)

    def get_by_key(self, bank_key: BankKey) -> Item:
        return self.get(bank_key.item_id)

    def contains(self, item_id: str) -> bool:
        return item_id in self

    def verify(self, item_id: str) -> None:
        if not self.contains(item_id):
            raise KeyError(f"'{item_id}' not in item registry.")


ITEM_REGISTRY = ItemRegistry()

ITEM_REGISTRY.load_from_dict(HELMS, item_cls=Armor)
ITEM_REGISTRY.load_from_dict(BODIES, item_cls=Armor)
ITEM_REGISTRY.load_from_dict(LEGS, item_cls=Armor)
ITEM_REGISTRY.load_from_dict(BOOTS, item_cls=Armor)
ITEM_REGISTRY.load_from_dict(GLOVES, item_cls=Armor)
ITEM_REGISTRY.load_from_dict(WEAPONS, item_cls=Weapon)
ITEM_REGISTRY.load_from_dict(OFFHANDS, item_cls=Armor)

ITEM_REGISTRY.load_from_dict(FISHING_RODS, item_cls=Tool)
ITEM_REGISTRY.load_from_dict(SECATEURS, item_cls=Tool)
ITEM_REGISTRY.load_from_dict(PICKAXES, item_cls=Tool)
ITEM_REGISTRY.load_from_dict(AXES, item_cls=Tool)

ITEM_REGISTRY.load_from_dict(COLLECTABLES, item_cls=Collectable)
ITEM_REGISTRY.load_from_dict(COOKABLES, item_cls=Cookable)
ITEM_REGISTRY.load_from_dict(CRAFTABLES, item_cls=Craftable)
ITEM_REGISTRY.load_from_dict(FISH, item_cls=Fish)
ITEM_REGISTRY.load_from_dict(MIXABLES, item_cls=Mixable)
ITEM_REGISTRY.load_from_dict(ORES, item_cls=Ore)
ITEM_REGISTRY.load_from_dict(SMELTABLES, item_cls=Smeltable)
ITEM_REGISTRY.load_from_dict(SMITHABLES, item_cls=Smithable)
ITEM_REGISTRY.load_from_dict(LOGS, item_cls=Log)

ITEM_REGISTRY.load_from_dict(MISC_ITEMS, item_cls=Item)
