from ...util.structures.Equippable import Armor
from ...util.structures.Stats import Stats


offhands = {
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
    'mithril kiteshield': Armor(
        name='mithril kiteshield',
        tier=20,
        stats=Stats({
            'physical_defense': 8,
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
    'rune kiteshield': Armor(
        name='rune kiteshield',
        tier=40,
        stats=Stats({
            'physical_defense': 14,
            'magical_barrier': 0,
            'evasiveness': 3,
        }),
    ),
    'orikalkum kiteshield': Armor(
        name='orikalkum kiteshield',
        tier=60,
        stats=Stats({
            'physical_defense': 20,
            'magical_barrier': 0,
            'evasiveness': 4,
        }),
    ),
    'necronium kiteshield': Armor(
        name='necronium kiteshield',
        tier=70,
        stats=Stats({
            'physical_defense': 24,
            'magical_barrier': 0,
            'evasiveness': 5,
        }),
    ),
    'bane kiteshield': Armor(
        name='bane kiteshield',
        tier=80,
        stats=Stats({
            'physical_defense': 27,
            'magical_barrier': 0,
            'evasiveness': 5,
        }),
    ),
    'elder kiteshield': Armor(
        name='elder kiteshield',
        tier=90,
        stats=Stats({
            'physical_defense': 30,
            'magical_barrier': 0,
            'evasiveness': 6,
        }),
    ),
}
