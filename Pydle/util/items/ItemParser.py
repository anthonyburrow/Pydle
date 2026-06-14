from .Item import Item
from .ItemInstance import ItemInstance
from .ItemRegistry import ITEM_REGISTRY, ItemRegistry
from .Quality import Quality


class ItemParser:
    def __init__(self, item_registry: ItemRegistry):
        self._item_registry: ItemRegistry = item_registry

        self.name_map: dict[str, tuple[str, Quality | None]] = {}
        self._build_lookup_map()

    def _build_lookup_map(self) -> None:
        for item_id, item in self._item_registry.items():
            if not item.supported_qualities:
                name: str = item.name.lower()
                self.name_map[name] = (item_id, None)
                continue

            for quality in item.supported_qualities:
                name: str = ItemInstance.get_name(item.name, quality).lower()
                self.name_map[name] = (item_id, quality)

    def get_base(self, item_name: str) -> Item:
        item_id: str = self.get_id_by_name(item_name)

        return ITEM_REGISTRY[item_id]

    def get_instance(self, item_name: str, quantity: int = 1) -> ItemInstance:
        item_id, quality = self.name_map[item_name.lower()]
        item_instance: ItemInstance = ItemInstance(
            item_id=item_id,
            quantity=quantity,
            quality=quality,
        )

        return item_instance

    def get_instance_by_id(
        self, item_id: str, quantity: int = 1
    ) -> ItemInstance:
        return ItemInstance(item_id=item_id, quantity=quantity)

    def get_id_by_name(self, item_name: str) -> str:
        instance_data: tuple[str, Quality | None] = self.name_map[
            item_name.lower()
        ]

        return instance_data[0]

    def is_valid_item_name(self, item_name: str) -> bool:
        return item_name in self.name_map


ITEM_PARSER = ItemParser(ITEM_REGISTRY)
