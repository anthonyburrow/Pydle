from typing import Self

from .BankKey import BankKey
from ..colors import color, color_theme
from ..visuals import centered_title
from ..items.ItemInstance import ItemInstance


class Bank(dict):

    def __init__(self, bank_dict: dict | None = None):
        bank_dict = bank_dict or {}
        self.load_from_dict(bank_dict)

    def add(self, items: ItemInstance | Self) -> Self:
        if isinstance(items, ItemInstance):
            return self._add_instance(items)
        elif isinstance(items, Bank):
            return self._add_bank(items)

        return self

    def _add_instance(self, item_instance: ItemInstance) -> Self:
        bank_key: BankKey = item_instance.get_key()

        if self.contains(item_instance):
            self[bank_key].quantity += item_instance.quantity
            return self

        self[bank_key] = item_instance

        return self

    def _add_bank(self, item_bank: Self) -> Self:
        for item_instance in item_bank.values():
            self._add_instance(item_instance)

        return self

    def remove(self, items: ItemInstance | Self) -> Self:
        if isinstance(items, ItemInstance):
            return self._remove_instance(items)
        elif isinstance(items, Bank):
            return self._remove_bank(items)

        return self

    def _remove_instance(self, item_instance: ItemInstance) -> Self:
        bank_key: BankKey = item_instance.get_key()
        quantity: int = item_instance.quantity

        if not self.contains(item_instance, check_quantity=True):
            item_id: str = item_instance.item_id
            raise KeyError(f'Bank does not contain {quantity}x {item_id}')

        new_quantity: int = self[bank_key].quantity - quantity

        if new_quantity <= 0:
            self.pop(bank_key)
            return self

        self[bank_key].quantity = new_quantity

        return self

    def _remove_bank(self, item_bank: Self) -> Self:
        for item_instance in item_bank.values():
            self._remove_instance(item_instance)

        return self

    def contains(
        self,
        items: ItemInstance | Self,
        check_quantity: bool = False
    ) -> bool:
        if isinstance(items, ItemInstance):
            return self._contains_instance(items, check_quantity=check_quantity)
        elif isinstance(items, Bank):
            return self._contains_bank(items, check_quantity=check_quantity)

    def _contains_instance(
        self,
        item_instance: ItemInstance,
        check_quantity: bool = False,
    ) -> bool:
        bank_key: BankKey = item_instance.get_key()

        if bank_key not in self:
            return False

        if not check_quantity:
            return True

        return self[bank_key].quantity >= item_instance.quantity

    def _contains_bank(
        self,
        item_bank: Self,
        check_quantity: bool = False,
    ) -> bool:
        for item_instance in item_bank.values():
            if not self._contains_instance(
                item_instance, check_quantity=check_quantity
            ):
                return False

        return True

    def quantity(self, bank_key: BankKey) -> int:
        if bank_key not in self:
            return 0

        item_instance: ItemInstance = self[bank_key]

        return item_instance.quantity

    def to_dict(self) -> dict[str, dict]:
        return {
            str(bank_key): item_instance.to_dict()
            for bank_key, item_instance in self.items()
        }

    def load_from_dict(self, data: dict[str, dict]) -> None:
        for instance_dict in data.values():
            item_instance: ItemInstance = ItemInstance.from_dict(instance_dict)
            bank_key: BankKey = item_instance.get_key()
            self[bank_key] = item_instance

    def list_concise(self) -> str:
        list_str: list = []
        for item_instance in self.values():
            list_str.append(f'{item_instance.quantity}x {item_instance}')
        msg = ', '.join(list_str)

        return msg

    def __str__(self) -> str:
        msg: list = []

        max_item_length: int = max([len(x.name) for x in self.values()])
        max_qty_length: int = max(len(str(x.quantity)) for x in self.values())
        total_length: int = max_item_length + max_qty_length + 6

        msg.append(centered_title('BANK', total_length))

        if not self:
            return '\n'.join(msg)

        for item_instance in self.value():
            qty_str = color(
                f'[{item_instance.quantity}]'.rjust(max_qty_length + 2),
                color_theme['UI_1']
            )
            msg.append(
                f'* {item_instance:<{max_item_length}}  {qty_str}'
            )

        msg = '\n'.join(msg)

        return msg
