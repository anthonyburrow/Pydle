from enum import Enum

from ...util.structures.Stats import Stats
from ...util.structures.LootTable import LootTable
from ...util.colors import color, color_theme


class MonsterTier(Enum):
    BASIC = 0
    SUPERIOR = 1
    BOSS = 2


class Monster:

    def __init__(
        self,
        # Info
        name: str,
        level: int = 1,
        tier: MonsterTier = MonsterTier.BASIC,
        XP: float = None,
        loot_table: LootTable = None,
        # Combat
        hitpoints: int = 100,
        stats: Stats = None,
    ):
        # Info
        self.name: str = name
        self.tier: MonsterTier = tier
        self.level: int = level
        if XP is None:
            self.XP: float = 4. * float(hitpoints)
        else:
            self.XP: float = XP
        self.loot_table = loot_table if loot_table is not None else LootTable()

        # Combat
        self.hitpoints: int = hitpoints
        self.max_hitpoints: int = hitpoints
        self.stats: Stats = stats

    def damage(self, amount: int) -> None:
        self.hitpoints = max(0, self.hitpoints - amount)

    def reset(self) -> None:
        self.hitpoints = self.max_hitpoints

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


monsters = {
    'goblin': {
        'name': 'goblin',
        'level': 1,
        'tier': MonsterTier.BASIC,
        'XP': 10.,
        'loot_table': (
            LootTable()
            .every('bones')
            .tertiary('coins', 0.5, 1)
        ),
        'hitpoints': 100,
        'stats': Stats({
            'ticks_per_action': 4,
            'attack_melee': 1,
            'defense_melee': 1,
        }),
    }
}
