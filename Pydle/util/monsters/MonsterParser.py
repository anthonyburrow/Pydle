from .MonsterInstance import MonsterInstance
from .MonsterRegistry import MonsterRegistry, MONSTER_REGISTRY


class MonsterParser:

    def __init__(self, monster_registry: MonsterRegistry):
        self._monster_registry: MonsterRegistry = monster_registry

        self._name_map: dict[str, dict[str, str]] = {}
        self._build_lookup_map()

    def _build_lookup_map(self) -> None:
        for monster_id, monster in self._monster_registry.items():
            name: str = monster.name.lower()
            self._name_map[name] = {
                'monster_id': monster_id,
            }

    def get_instance(self, monster_name: str) -> MonsterInstance | None:
        instance_kwargs: dict[str, str] | None = self._name_map.get(monster_name.lower())

        if not instance_kwargs:
            return None

        monster_instance = MonsterInstance(**instance_kwargs)

        return monster_instance


MONSTER_PARSER = MonsterParser(MONSTER_REGISTRY)
