from .ItemRegistry import ItemRegistry, ITEM_REGISTRY
from .items.Item import Item, ItemInstance
from .Command import Command


class ItemParser:

    def __init__(self, item_registry: ItemRegistry):
        self._item_registry: ItemRegistry = item_registry

        self._name_map: dict[str, dict] = {}
        self._build_lookup_map()

    def _build_lookup_map(self) -> None:
        for item_id, item in self._item_registry.items():
            if not item.supported_qualities:
                name: str = item.name.lower()
                self._name_map[name] = {
                    'item_id': item_id,
                }
                continue

            for quality in item.supported_qualities:
                name: str = ItemInstance.get_name().lower()
                self._name_map[name] = {
                    'item_id': item_id,
                    'quality': quality,
                }

    def get_base(self, item_name: str) -> Item | None:
        instance_kwargs: dict = self._name_map.get(item_name)

        if not instance_kwargs:
            return None

        item_id: str = instance_kwargs['item_id']

        return ITEM_REGISTRY[item_id]

    def get_instance(self, item_name: str, quantity: int = 1) -> ItemInstance | None:
        instance_kwargs: dict = self._name_map.get(item_name.lower())

        if not instance_kwargs:
            return None

        instance_kwargs['quantity'] = quantity
        item_instance = ItemInstance(**instance_kwargs)

        return item_instance

    def get_instance_by_command(self, command: Command) -> ItemInstance | None:
        return self.get_instance(command.argument, command.quantity)

    def get_instance_by_id(self, item_id: str) -> ItemInstance | None:
        return ItemInstance(item_id=item_id)


ITEM_PARSER = ItemParser(ITEM_REGISTRY)
