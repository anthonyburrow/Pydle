from ...util.structures.Equippable import Armor
from ...util.structures.Stats import Stats


BODIES = {
    'copper chestplate': Armor(
        name='copper chestplate',
        tier=1,
        stats=Stats({
            'physical_defense': 2,
            'magical_barrier': 0,
            'evasiveness': 0,
        }),
    ),
    'iron chestplate': Armor(
        name='iron chestplate',
        tier=10,
        stats=Stats({
            'physical_defense': 4,
            'magical_barrier': 1,
            'evasiveness': 1,
        }),
    ),
    'steel chestplate': Armor(
        name='steel chestplate',
        tier=15,
        stats=Stats({
            'physical_defense': 6,
            'magical_barrier': 1,
            'evasiveness': 1,
        }),
    ),
    'adamant chestplate': Armor(
        name='adamant chestplate',
        tier=30,
        stats=Stats({
            'physical_defense': 11,
            'magical_barrier': 2,
            'evasiveness': 2,
        }),
    ),
}
