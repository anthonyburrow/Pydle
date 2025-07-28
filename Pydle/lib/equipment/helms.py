from ...util.structures.Equippable import Armor
from ...util.structures.Stats import Stats


helms = {
    'copper helm': Armor(
        name='copper helm',
        tier=1,
        stats=Stats({
            'physical_defense': 1,
            'magical_barrier': 0,
            'evasiveness': 0,
        }),
    ),
    'iron helm': Armor(
        name='iron helm',
        tier=10,
        stats=Stats({
            'physical_defense': 3,
            'magical_barrier': 0,
            'evasiveness': 0,
        }),
    ),
    'steel helm': Armor(
        name='steel helm',
        tier=15,
        stats=Stats({
            'physical_defense': 4,
            'magical_barrier': 1,
            'evasiveness': 1,
        }),
    ),
    'adamant helm': Armor(
        name='adamant helm',
        tier=30,
        stats=Stats({
            'physical_defense': 7,
            'magical_barrier': 1,
            'evasiveness': 1,
        }),
    ),
}
