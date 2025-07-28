from ...util.structures.Equippable import Armor
from ...util.structures.Stats import Stats


BOOTS = {
    'copper boots': Armor(
        name='copper boots',
        tier=1,
        stats=Stats({
            'physical_defense': 0,
            'magical_barrier': 0,
            'evasiveness': 0,
        }),
    ),
    'iron boots': Armor(
        name='iron boots',
        tier=10,
        stats=Stats({
            'physical_defense': 2,
            'magical_barrier': 0,
            'evasiveness': 0,
        }),
    ),
    'steel boots': Armor(
        name='steel boots',
        tier=15,
        stats=Stats({
            'physical_defense': 2,
            'magical_barrier': 0,
            'evasiveness': 0,
        }),
    ),
    'adamant boots': Armor(
        name='adamant boots',
        tier=30,
        stats=Stats({
            'physical_defense': 4,
            'magical_barrier': 1,
            'evasiveness': 1,
        }),
    ),
}
