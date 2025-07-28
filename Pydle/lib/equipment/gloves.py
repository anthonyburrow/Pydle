from ...util.structures.Equippable import Armor
from ...util.structures.Stats import Stats


GLOVES = {
    'copper gauntlets': Armor(
        name='copper gauntlets',
        tier=1,
        stats=Stats({
            'physical_defense': 0,
            'magical_barrier': 0,
            'evasiveness': 0,
        })
    ),
    'iron gauntlets': Armor(
        name='iron gauntlets',
        tier=10,
        stats=Stats({
            'physical_defense': 2,
            'magical_barrier': 0,
            'evasiveness': 0,
        })
    ),
    'steel gauntlets': Armor(
        name='steel gauntlets',
        tier=15,
        stats=Stats({
            'physical_defense': 2,
            'magical_barrier': 0,
            'evasiveness': 0,
        }),
    ),
    'adamant gauntlets': Armor(
        name='adamant gauntlets',
        tier=30,
        stats=Stats({
            'physical_defense': 4,
            'magical_barrier': 1,
            'evasiveness': 1,
        }),
    ),
}
