from ...util.structures.Equippable import Armor
from ...util.structures.Stats import Stats


bodies = {
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
    'mithril chestplate': Armor(
        name='mithril chestplate',
        tier=20,
        stats=Stats({
            'physical_defense': 8,
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
    'rune chestplate': Armor(
        name='rune chestplate',
        tier=40,
        stats=Stats({
            'physical_defense': 14,
            'magical_barrier': 3,
            'evasiveness': 3,
        }),
    ),
    'orikalkum chestplate': Armor(
        name='orikalkum chestplate',
        tier=60,
        stats=Stats({
            'physical_defense': 20,
            'magical_barrier': 4,
            'evasiveness': 4,
        }),
    ),
    'necronium chestplate': Armor(
        name='necronium chestplate',
        tier=70,
        stats=Stats({
            'physical_defense': 24,
            'magical_barrier': 5,
            'evasiveness': 5,
        }),
    ),
    'bane chestplate': Armor(
        name='bane chestplate',
        tier=80,
        stats=Stats({
            'physical_defense': 27,
            'magical_barrier': 5,
            'evasiveness': 5,
        }),
    ),
    'elder chestplate': Armor(
        name='elder chestplate',
        tier=90,
        stats=Stats({
            'physical_defense': 30,
            'magical_barrier': 6,
            'evasiveness': 6,
        }),
    ),
}
