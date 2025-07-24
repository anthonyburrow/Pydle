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
    'mithril helm': Armor(
        name='mithril helm',
        tier=20,
        stats=Stats({
            'physical_defense': 5,
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
    'rune helm': Armor(
        name='rune helm',
        tier=40,
        stats=Stats({
            'physical_defense': 9,
            'magical_barrier': 2,
            'evasiveness': 2,
        }),
    ),
    'orikalkum helm': Armor(
        name='orikalkum helm',
        tier=60,
        stats=Stats({
            'physical_defense': 14,
            'magical_barrier': 3,
            'evasiveness': 3,
        }),
    ),
    'necronium helm': Armor(
        name='necronium helm',
        tier=70,
        stats=Stats({
            'physical_defense': 16,
            'magical_barrier': 3,
            'evasiveness': 3,
        }),
    ),
    'bane helm': Armor(
        name='bane helm',
        tier=80,
        stats=Stats({
            'physical_defense': 18,
            'magical_barrier': 4,
            'evasiveness': 4,
        }),
    ),
    'elder helm': Armor(
        name='elder helm',
        tier=90,
        stats=Stats({
            'physical_defense': 20,
            'magical_barrier': 4,
            'evasiveness': 4,
        }),
    ),
}
