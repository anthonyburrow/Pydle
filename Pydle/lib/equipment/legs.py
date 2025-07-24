from ...util.structures.Equippable import Armor
from ...util.structures.Stats import Stats


legs = {
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
    'mithril platelegs': Armor(
        name='mithril platelegs',
        tier=20,
        stats=Stats({
            'physical_defense': 8,
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
    'rune platelegs': Armor(
        name='rune platelegs',
        tier=40,
        stats=Stats({
            'physical_defense': 14,
            'magical_barrier': 3,
            'evasiveness': 3,
        }),
    ),
    'orikalkum platelegs': Armor(
        name='orikalkum platelegs',
        tier=60,
        stats=Stats({
            'physical_defense': 20,
            'magical_barrier': 4,
            'evasiveness': 4,
        }),
    ),
    'necronium platelegs': Armor(
        name='necronium platelegs',
        tier=70,
        stats=Stats({
            'physical_defense': 24,
            'magical_barrier': 5,
            'evasiveness': 5,
        }),
    ),
    'bane platelegs': Armor(
        name='bane platelegs',
        tier=80,
        stats=Stats({
            'physical_defense': 27,
            'magical_barrier': 5,
            'evasiveness': 5,
        }),
    ),
    'elder platelegs': Armor(
        name='elder platelegs',
        tier=90,
        stats=Stats({
            'physical_defense': 30,
            'magical_barrier': 6,
            'evasiveness': 6,
        }),
    ),
}
