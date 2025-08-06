from .ItemRegistry import ItemRegistry, ITEM_REGISTRY
from .items.Item import ItemInstance
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

    def get_instance(self, command: Command) -> ItemInstance | None:
        instance_kwargs: dict = self._name_map.get(command.argument)

        if not instance_kwargs:
            return None

        item_instance = ItemInstance(**instance_kwargs)

        return item_instance


ITEM_PARSER = ItemParser(ITEM_REGISTRY)
