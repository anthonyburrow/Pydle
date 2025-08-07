from .items.Item import Item
from .structures.Bank import BankKey


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
            self.register(item_id, item)

    def get_by_key(self, bank_key: BankKey) -> Item:
        return self.get(bank_key.item_id)

    def contains(self, item_id: str) -> bool:
        return item_id in self

    def verify(self, item_id: str) -> None:
        if not self.contains(item_id):
            raise KeyError(f"'{item_id}' not in item registry.")


ITEM_REGISTRY = ItemRegistry()

# ITEMS.load_from_dict(RAW_SMELTABLES, item_cls=Smeltable)
