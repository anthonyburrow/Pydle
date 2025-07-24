from ...util.structures.Equippable import Armor
from ...util.structures.Stats import Stats


boots = {
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
    'mithril boots': Armor(
        name='mithril boots',
        tier=20,
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
    'rune boots': Armor(
        name='rune boots',
        tier=40,
        stats=Stats({
            'physical_defense': 5,
            'magical_barrier': 1,
            'evasiveness': 1,
        }),
    ),
    'orikalkum boots': Armor(
        name='orikalkum boots',
        tier=60,
        stats=Stats({
            'physical_defense': 7,
            'magical_barrier': 1,
            'evasiveness': 1,
        }),
    ),
    'necronium boots': Armor(
        name='necronium boots',
        tier=70,
        stats=Stats({
            'physical_defense': 8,
            'magical_barrier': 2,
            'evasiveness': 2,
        }),
    ),
    'bane boots': Armor(
        name='bane boots',
        tier=80,
        stats=Stats({
            'physical_defense': 9,
            'magical_barrier': 2,
            'evasiveness': 2,
        }),
    ),
    'elder boots': Armor(
        name='elder boots',
        tier=90,
        stats=Stats({
            'physical_defense': 10,
            'magical_barrier': 2,
            'evasiveness': 2,
        }),
    ),
}
