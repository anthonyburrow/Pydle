from ...util.structures.Monster import MonsterTier
from ...util.structures.Stats import Stats
from ...util.structures.LootTable import LootTable


monsters = {
    'goblin': {
        'name': 'goblin',
        'level': 1,
        'tier': MonsterTier.BASIC,
        'xp': 10.,
        'loot_table': (
            LootTable()
            .every('bones')
            .tertiary('coins', 0.5, 1)
        ),
        'hitpoints': 100,
        'attack_speed': 4,
        'stats': Stats({
            'physical_strength': 1,
            'physical_defense': 1,
        }),
    }
}
