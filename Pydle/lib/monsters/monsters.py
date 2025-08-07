from ...util.ItemParser import ITEM_PARSER
from ...util.structures.Monster import MonsterTier
from ...util.structures.LootTable import LootTable


MONSTERS = {
    'goblin': {
        'name': 'goblin',
        'level': 1,
        'tier': MonsterTier.BASIC,
        'xp': 10.,
        'loot_table': (
            LootTable()
            .every(ITEM_PARSER.get_instance('bones'))
            .tertiary(ITEM_PARSER.get_instance('coins'), 0.5)
        ),
        'hitpoints': 100,
        'attack_speed': 4,
        'stats': {
            'physical_strength': 1,
            'physical_defense': 1,
        },
    }
}
