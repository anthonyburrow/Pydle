from ..colors import color, COLOR_BANK1


class Bank:

    def __init__(self, items: dict = None):
        if items is None:
            items = {}
        self._items = items

        # Remove zero/negative quantities
        self._items = {item: quantity for item, quantity in self._items.items()
                       if quantity > 0}

    def add(self, items=None, *args, **kwargs) -> None:
        if isinstance(items, str):
            self._add_item(items, *args, **kwargs)
        elif isinstance(items, dict):
            self._add_dict(items)
        elif isinstance(items, Bank):
            self._add_bank(items)

    def remove(self, item: str, quantity: int) -> None:
        if not self.contains(item, quantity):
            raise ValueError(f'Bank does not contain {quantity}x {item}')

        new_quantity = self._items[item] - quantity

        if new_quantity <= 0:
            self._items.pop(item)
        else:
            self._items[item] = new_quantity

    def contains(self, item: str, quantity: int = None, *args, **kwargs) -> bool:
        # TODO: Add bank optional argument instead of single item
        if item.lower() not in self._items:
            return False

        if quantity is None:
            return True

        in_bank = self._items[item]

        return in_bank >= quantity

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

    def __str__(self) -> str:
        spacing = '  '
        title = 'BANK'
        separator = '---'
        header = f'{spacing}{title}\n{spacing}{separator}\n{spacing}'

        if not self._items:
            msg = f'\n{header}\n'
            return msg

        items_str = []
        for item, quantity in self._items.items():
            qty = color(f'({quantity}x)', COLOR_BANK1)
            items_str.append(f'{item.capitalize()} {qty}')
        msg = '\n' + header + f'\n{spacing}'.join(items_str) + '\n'

        return msg

    def __bool__(self) -> bool:
        return bool(self._items)

    def _add_item(self, item: str, quantity: int = 1) -> None:
        if quantity < 0:
            raise ValueError(f'Tried to add negative {item} to bank')

        if quantity == 0:
            return

        item = item.lower()
        if not self.contains(item):
            self._items[item] = quantity
            return

        self._items[item] += quantity

    def _add_dict(self, items: dict) -> None:
        for item, quantity in items.items():
            self._add_item(item, quantity)

    def _add_bank(self, bank) -> None:
        # Could just make this a __add__, etc dunder
        for item, quantity in bank._items.items():
            self._add_item(item, quantity)
