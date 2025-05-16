from ...util.structures.Stats import Stats
from ...util.structures.LootTable import LootTable


class Monster:

    def __init__(
        self,
        name: str,
        level: int,
        XP: float,
        loot_table: LootTable,
        # Combat
        hitpoints: int,
        stats: Stats,
    ):
        self.name: str = name
        self.XP: float = XP
        self.level: int = level

        # Combat
        self.hitpoints: int = hitpoints,
        self.stats: Stats = stats,


monsters = {
    'goblin': Monster(
        name='goblin',
        level=3,
        XP=10.,
        loot_table=
            LootTable().every('bones'),
        hitpoints=5,
        stats=Stats({
            'attack_melee': 1,
            'defense_melee': 1,
        }),
    )
}
