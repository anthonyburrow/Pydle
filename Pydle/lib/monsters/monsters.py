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
            'ticks_per_action': 4,
            'attack_melee': 1,
            'defense_melee': 1,
        }),
    }
}
