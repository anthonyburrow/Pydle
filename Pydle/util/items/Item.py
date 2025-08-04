from abc import ABC
from typing import Self

from .Quality import Quality
from ..ItemRegistry import ITEM_REGISTRY
from ..colors import color, color_theme
from ..structures.Bank import BankKey


class Item(ABC):
    def __init__(self, item_id: str, name: str):
        self.item_id: str = item_id
        self.name: str = name

    def __repr__(self):
        return f'<Item id={self.item_id}, name={self.name}>'

    # def to_dict(self) -> dict:
    #     return {'item_id': self.item_id, 'name': self.name}

    # def display_name(self, quality: str | None = None) -> str:
    #     return f'{quality} {self.name}'.strip().title()

    def __str__(self):
        return self.name


class ItemInstance:
    def __init__(
        self,
        item_id: str,
        quantity: int = 1,
        quality: Quality | None = None
    ):
        ITEM_REGISTRY.verify(item_id)

        self.quantity: int = quantity
        self.quality: Quality | None = quality

        self.set_name()

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

    def get_key(self) -> BankKey:
        return BankKey(self.item_id, self.quality)

    def set_name(self) -> None:
        if not self.quality:
            return

        quality_str: str = f'{self.quality}'
        self.name: str = f'{quality_str} {self.base.name}'

    def __str__(self) -> str:
        if not self.quality:
            return str(self.base)

        if self.quality == Quality.POOR or self.quality == Quality.GOOD:
            theme: str = 'quality_poor'
        elif self.quality == Quality.GREAT or self.quality == Quality.SUPERIOR:
            theme: str = 'quality_good'
        elif self.quality == Quality.MASTER:
            theme: str = 'quality_master'

        return color(self.name, color_theme[theme])

    def __getattr__(self, name):
        try:
            return getattr(self.base, name)
        except AttributeError:
            raise AttributeError(
                f"'{self.__class__.__name__}' object or its underlying "
                f"'{self.base.__class__.__name__}' object has no attribute '{name}'"
            )
