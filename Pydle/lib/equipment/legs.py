from ...util.structures.Equippable import Armor
from ...util.structures.Stats import Stats


LEGS = {
    'copper platelegs': Armor(
        name='copper platelegs',
        tier=1,
        stats=Stats({
            'physical_defense': 2,
            'magical_barrier': 0,
            'evasiveness': 0,
        }),
    ),
    'iron platelegs': Armor(
        name='iron platelegs',
        tier=10,
        stats=Stats({
            'physical_defense': 4,
            'magical_barrier': 1,
            'evasiveness': 1,
        }),
    ),
    'steel platelegs': Armor(
        name='steel platelegs',
        tier=15,
        stats=Stats({
            'physical_defense': 6,
            'magical_barrier': 1,
            'evasiveness': 1,
        }),
    ),
    'adamant platelegs': Armor(
        name='adamant platelegs',
        tier=30,
        stats=Stats({
            'physical_defense': 11,
            'magical_barrier': 2,
            'evasiveness': 2,
        }),
    ),
}
