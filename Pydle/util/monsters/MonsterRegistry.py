from .Monster import Monster
from ...lib.monsters import MONSTERS


class MonsterRegistry(dict):
    def __init__(self):
        pass

    def register(self, monster_id: str, monster: Monster):
        if monster_id in self:
            raise ValueError(f'Duplicate monster_id: {monster_id}')
        self[monster_id] = monster

    def load_from_dict(self, monster_dict: dict[str, dict]):
        for monster_id, monster_kwargs in monster_dict.items():
            monster = Monster(monster_id=monster_id, **monster_kwargs)
            self.register(monster_id, monster)

    def contains(self, monster_id: str) -> bool:
        return monster_id in self

    def verify(self, monster_id: str) -> None:
        if not self.contains(monster_id):
            raise KeyError(f"'{monster_id}' not in monster registry.")


MONSTER_REGISTRY = MonsterRegistry()

MONSTER_REGISTRY.load_from_dict(MONSTERS)
