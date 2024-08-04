from ..colors import color, color_theme


class Bank:

    def __init__(self, items: dict = None):
        if items is None:
            items = {}
        self._items = items

        # Remove zero/negative quantities
        self._items = {item: quantity for item, quantity in self._items.items()
                       if quantity > 0}

    def add(self, items: str | dict, *args, **kwargs):
        if isinstance(items, str):
            return self._add_item(items, *args, **kwargs)
        elif isinstance(items, dict):
            return self._add_dict(items)
        elif isinstance(items, Bank):
            return self._add_bank(items)

    def _add_item(self, item: str, quantity: int = 1):
        if quantity < 0:
            raise ValueError(f'Tried to add negative {item} to bank')

        if quantity == 0:
            return

        item = item.lower()
        if not self.contains(item):
            self._items[item] = quantity
            return

        self._items[item] += quantity

    def _add_dict(self, items: dict):
        for item, quantity in items.items():
            self._add_item(item, quantity)

    def _add_bank(self, bank):
        # Could just make this a __add__, etc dunder
        for item, quantity in bank._items.items():
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

        new_quantity = self._items[item] - quantity

        if new_quantity <= 0:
            self._items.pop(item)
        else:
            self._items[item] = new_quantity

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
        if item.lower() not in self._items:
            return False

        if quantity is None:
            return True

        in_bank = self._items[item]

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

        return self._items[item]

    def list_concise(self) -> str:
        items_str = []
        for item, quantity in self._items.items():
            items_str.append(f'{quantity}x {item}')
        msg = ', '.join(items_str)

        return msg

    @property
    def items(self):
        return self._items

    def __str__(self) -> str:
        msg: list = []

        msg.append('BANK')
        msg.append('---')

        if not self._items:
            return msg

        for item, quantity in self._items.items():
            qty = color(f'({quantity}x)', color_theme['UI_1'])
            msg.append(f'{item.capitalize()} {qty}')

        msg = f'\n'.join(msg)

        return msg

    def __bool__(self) -> bool:
        return bool(self._items)


