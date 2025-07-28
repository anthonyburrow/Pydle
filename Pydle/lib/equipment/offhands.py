from ...util.structures.Equippable import Armor
from ...util.structures.Stats import Stats


OFFHANDS = {
    'copper kiteshield': Armor(
        name='copper kiteshield',
        tier=1,
        stats=Stats({
            'physical_defense': 2,
            'magical_barrier': 0,
            'evasiveness': 0,
        }),
    ),
    'iron kiteshield': Armor(
        name='iron kiteshield',
        tier=10,
        stats=Stats({
            'physical_defense': 4,
            'magical_barrier': 0,
            'evasiveness': 1,
        }),
    ),
    'steel kiteshield': Armor(
        name='steel kiteshield',
        tier=15,
        stats=Stats({
            'physical_defense': 6,
            'magical_barrier': 0,
            'evasiveness': 1,
        }),
    ),
    'adamant kiteshield': Armor(
        name='adamant kiteshield',
        tier=30,
        stats=Stats({
            'physical_defense': 11,
            'magical_barrier': 0,
            'evasiveness': 2,
        }),
    ),
}
