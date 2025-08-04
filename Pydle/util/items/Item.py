from abc import ABC
from typing import Self

from .Quality import Quality
from ..ItemRegistry import ItemRegistry
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
        return ItemRegistry[self.item_id]

    def get_key(self) -> BankKey:
        return BankKey(self.item_id, self.quality)

    def __str__(self) -> str:
        quality_str: str = self.quality.label if self.quality else ''
        return f'{quality_str}{self.base}'

    def __getattr__(self, name):
        try:
            return getattr(self.base, name)
        except AttributeError:
            raise AttributeError(
                f"'{self.__class__.__name__}' object or its underlying "
                f"'{self.base.__class__.__name__}' object has no attribute '{name}'"
            )
