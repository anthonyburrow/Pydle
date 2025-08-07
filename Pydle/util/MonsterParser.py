from .MonsterRegistry import MonsterRegistry, MONSTER_REGISTRY
from .structures.Monster import MonsterInstance
from .Command import Command


class MonsterParser:

    def __init__(self, monster_registry: MonsterRegistry):
        self._monster_registry: MonsterRegistry = monster_registry

        self._name_map: dict[str, dict] = {}
        self._build_lookup_map()

    def _build_lookup_map(self) -> None:
        for monster_id, monster in self._monster_registry.items():
            name: str = monster.name.lower()
            self._name_map[name] = {
                'monster_id': monster_id,
            }
            continue

    def get_instance(self, monster_name: str) -> MonsterInstance | None:
        instance_kwargs: dict = self._name_map.get(monster_name.lower())

        if not instance_kwargs:
            return None

        monster_instance = MonsterInstance(**instance_kwargs)

        return monster_instance

    def get_instance_by_command(self, command: Command) -> MonsterInstance | None:
        return self.get_instance(command.argument)


MONSTER_PARSER = MonsterParser(MONSTER_REGISTRY)
