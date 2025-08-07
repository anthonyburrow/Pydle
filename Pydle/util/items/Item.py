from abc import ABC
from typing import Self

from .ItemRegistry import ITEM_REGISTRY
from .Quality import Quality
from ..colors import color, color_theme
from ..player.Bank import BankKey


class Item(ABC):
    def __init__(self, item_id: str, name: str, supported_qualities=None):
        self.item_id: str = item_id
        self.name: str = name
        self.supported_qualities: list[Quality] = supported_qualities or []

    def __repr__(self):
        return f'<Item id={self.item_id}, name={self.name}>'

    def __str__(self):
        return self.name.title()


class ItemInstance:

    def __init__(
        self,
        item_id: str,
        quantity: int = 1,
        quality: Quality | None = None
    ):
        ITEM_REGISTRY.verify(item_id)

        self.item_id: str = item_id
        self.quantity: int = quantity
        self.quality: Quality | None = quality

        self.name = ItemInstance.get_name(self.name, self.quality)

    def to_dict(self) -> dict:
        return {
            'item_id': self.item_id,
            'quantity': self.quantity,
            'quality': self.quality.value if self.quality is not None else None
        }

    @staticmethod
    def from_dict(cls, data: dict) -> Self:
        return cls(
            item_id=data['item_id'],
            quantity=data['quantity'],
            quality=Quality.from_value(data.get('quality'))
        )

    @property
    def base(self) -> Item:
        return ITEM_REGISTRY[self.item_id]

    def set_quantity(self, quantity: int) -> None:
        self.quantity = quantity

    def get_key(self) -> BankKey:
        return BankKey(self.item_id, self.quality)

    @staticmethod
    def get_name(base_name: str, quality: Quality) -> str:
        if not quality:
            return base_name

        return f'{quality} {base_name}'

    def copy(self, **overrides):
        data = self.__dict__.copy()
        data.update(overrides)
        return ItemInstance(**data)

    def __str__(self) -> str:
        if not self.quality:
            return str(self.base)

        if self.quality == Quality.POOR or self.quality == Quality.GOOD:
            theme: str = 'quality_poor'
        elif self.quality == Quality.GREAT or self.quality == Quality.SUPERIOR:
            theme: str = 'quality_good'
        elif self.quality == Quality.MASTER:
            theme: str = 'quality_master'

        return color(self.name.title(), color_theme[theme])

    def __getattr__(self, name):
        try:
            return getattr(self.base, name)
        except AttributeError:
            raise AttributeError(
                f"'{self.__class__.__name__}' object or its underlying "
                f"'{self.base.__class__.__name__}' object has no attribute '{name}'"
            )

    def __eq__(self, other) -> bool:
        if not isinstance(other, ItemInstance):
            return False

        return (
            self.item_id == other.item_id and
            self.quantity == other.quantity and
            self.quality == other.quality
        )
