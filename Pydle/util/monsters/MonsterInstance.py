from .Monster import Monster
from .MonsterRegistry import MONSTER_REGISTRY


class MonsterInstance:

    def __init__(self, monster_id: str):
        MONSTER_REGISTRY.verify(monster_id)

        self.monster_id: str = monster_id
        self.hitpoints: int = self.base.hitpoints

    def damage(self, amount: int) -> None:
        self.hitpoints = max(0, self.hitpoints - amount)

    @property
    def base(self) -> Monster:
        return MONSTER_REGISTRY[self.monster_id]

    def __getattr__(self, name):
        try:
            return getattr(self.base, name)
        except AttributeError:
            raise AttributeError(
                f"'{self.__class__.__name__}' object or its underlying "
                f"'{self.base.__class__.__name__}' object has no attribute '{name}'"
            )
