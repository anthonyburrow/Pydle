from ...util.structures.Monster import MonsterTier
from ...util.structures.Stats import Stats
from ...util.structures.LootTable import LootTable


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
            'attack_speed': 4,
            'physical_strength': 1,
            'physical_defense': 1,
        }),
    }
}
