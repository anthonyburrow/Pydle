from ..colors import color, color_theme
from ..item_registry import ITEMS


class Bank(dict):

    def __init__(self, items: dict = None):
        if items is not None:
            self.add(items)

    def add(self, items: str | dict, *args, **kwargs):
        if isinstance(items, str):
            return self._add_item(items, *args, **kwargs)
        elif isinstance(items, dict):
            return self._add_dict(items)

    def _add_item(self, item: str, quantity: int = 1):
        if quantity <= 0:
            return

        item = item.lower()

        if item not in ITEMS:
            raise ValueError(f'"{item}" is not a valid item --- check registry.')

        if not self.contains(item):
            self[item] = quantity
            return

        self[item] += quantity

    def _add_dict(self, items: dict):
        for item, quantity in items.items():
            self._add_item(item, quantity)

    # Remove items
    def remove(self, items: str | dict, *args, **kwargs):
        if isinstance(items, str):
            return self._remove_item(items, *args, **kwargs)
        elif isinstance(items, dict):
            return self._remove_dict(items)

    def _remove_item(self, item: str, quantity: int):
        if not self.contains(item, quantity):
            raise KeyError(f'Bank does not contain {quantity}x {item}')

        new_quantity = self[item] - quantity

        if new_quantity <= 0:
            self.pop(item)
        else:
            self[item] = new_quantity

    def _remove_dict(self, items: dict):
        for item, quantity in items.items():
            self._remove_item(item, quantity)

    # Contains items
    def contains(self, items: str | dict, *args, **kwargs) -> bool:
        if isinstance(items, str):
            return self._contains_item(items, *args, **kwargs)
        elif isinstance(items, dict):
            return self._contains_dict(items)

    def _contains_item(self, item: str, quantity: int = None) -> bool:
        if item not in self:
            return False

        if quantity is None:
            return True

        in_bank = self[item]

        return in_bank >= quantity

    def _contains_dict(self, items: dict) -> bool:
        for item, quantity in items.items():
            if not self._contains_item(item, quantity):
                return False

        return True

    # Quantity
    def quantity(self, item: str) -> int:
        if not self.contains(item):
            return 0

        return self[item]

    def get_items(self) -> dict:
        return {item: qty for item, qty in self.items()}

    def list_concise(self) -> str:
        items_str = []
        for item, quantity in self.items():
            items_str.append(f'{quantity}x {item}')
        msg = ', '.join(items_str)

        return msg

    def __str__(self) -> str:
        msg: list = []

        msg.append('BANK')
        msg.append('---')

        if not self:
            return f'\n'.join(msg)

        for item, quantity in self.items():
            qty = color(f'({quantity}x)', color_theme['UI_1'])
            msg.append(f'{item.capitalize()} {qty}')

        msg = f'\n'.join(msg)

        return msg

    def __eq__(self, other_items) -> bool:
        if not self._contains_dict(other_items):
            return False

        if not other_items._contains_dict(self):
            return False

        for item, quantity in other_items.items():
            if self[item] != quantity:
                return False

        return True
