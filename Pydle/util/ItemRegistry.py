from dataclasses import dataclass


@dataclass(frozen=True)
class ItemKey:
    item_id: str
    quality: Optional[str] = None

    def __hash__(self):
        return hash((self.item_id, self.quality))


class ItemRegistry(dict):
    def __init__(self):
        pass

    def register(self, item_id: str, obj: Item):
        if item_id in self:
            raise ValueError(f'Duplicate item_id: {item_id}')
        self[item_id] = obj

    def load_from_dict(self, item_dict: dict[str, dict], item_cls: type[Item]):
        for item_id, item_kwargs in item_dict.items():
            obj = item_cls(item_id=item_id, **item_kwargs)
            self.register(item_id, obj)

    def get(self, item_id: str) -> Item:
        return self[item_id]

    def get_by_key(self, key: ItemKey) -> Item:
        return self.get(key.item_id)

    def contains(self, item_id: str) -> bool:
        return item_id in self

    def verify(self, item_id: str) -> None:
        if not contains(item_id):
            raise KeyError(f"'{item_id}' not in item registry.")

    # def display_name(self, key: ItemKey) -> str:
    #     item = self.get(key.item_id)
    #     name = getattr(item, "name", key.item_id)
    #     return f"{key.quality} {name}".strip().title() if key.quality else name


ITEM_REGISTRY = ItemRegistry()

# ITEMS.load_from_dict(RAW_SMELTABLES, item_cls=Smeltable)
