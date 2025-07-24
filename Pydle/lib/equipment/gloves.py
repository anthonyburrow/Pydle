from ...util.structures.Equippable import Armor
from ...util.structures.Stats import Stats


gloves = {
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
    'mithril gauntlets': Armor(
        name='mithril gauntlets',
        tier=20,
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
    'rune gauntlets': Armor(
        name='rune gauntlets',
        tier=40,
        stats=Stats({
            'physical_defense': 5,
            'magical_barrier': 1,
            'evasiveness': 1,
        }),
    ),
    'orikalkum gauntlets': Armor(
        name='orikalkum gauntlets',
        tier=60,
        stats=Stats({
            'physical_defense': 7,
            'magical_barrier': 1,
            'evasiveness': 1,
        }),
    ),
    'necronium gauntlets': Armor(
        name='necronium gauntlets',
        tier=70,
        stats=Stats({
            'physical_defense': 8,
            'magical_barrier': 2,
            'evasiveness': 2,
        }),
    ),
    'bane gauntlets': Armor(
        name='bane gauntlets',
        tier=80,
        stats=Stats({
            'physical_defense': 9,
            'magical_barrier': 2,
            'evasiveness': 2,
        }),
    ),
    'elder gauntlets': Armor(
        name='elder gauntlets',
        tier=90,
        stats=Stats({
            'physical_defense': 10,
            'magical_barrier': 2,
            'evasiveness': 2,
        }),
    ),
}
