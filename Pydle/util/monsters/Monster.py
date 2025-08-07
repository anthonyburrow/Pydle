from enum import Enum

from ..colors import color, color_theme
from ..player.Stats import Stats
from ..structures.LootTable import LootTable


class MonsterTier(Enum):
    BASIC = 0
    SUPERIOR = 1
    BOSS = 2


class Monster:

    def __init__(
        self,
        # Info
        monster_id: str,
        name: str,
        level: int = 1,
        tier: MonsterTier = MonsterTier.BASIC,
        loot_table: LootTable = None,
        # Combat
        max_hitpoints: int = 100,
        attack_speed: int = 3,
        stats_dict: dict[str, int] = None,
    ):
        # Info
        self.monster_id: str = monster_id
        self.name: str = name
        self.level: int = level
        self.tier: MonsterTier = tier
        self.loot_table = loot_table or LootTable()

        # Combat
        self.max_hitpoints: int = max_hitpoints
        self.attack_speed: int = attack_speed
        self.stats: Stats = Stats(stats_dict)

    def get_stat(self, stat_key: str) -> int:
        return self.stats[stat_key]

    def __str__(self):
        if self.tier == MonsterTier.BASIC:
            theme: str = 'monster_basic'
        elif self.tier == MonsterTier.SUPERIOR:
            theme: str = 'monster_superior'
        elif self.tier == MonsterTier.BOSS:
            theme: str = 'monster_boss'

        return color(self.name, color_theme[theme])
