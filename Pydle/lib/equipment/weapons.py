from ...util.structures.Equippable import Weapon
from ...util.structures.Stats import Stats


weapons = {
    'copper longsword': Weapon(
        name='copper longsword',
        tier=1,
        attack_speed=3,
        stats=Stats({
            'physical_strength': 2,
            'magical_power': 0,
            'accuracy': 0,
        }),
    ),
    'iron longsword': Weapon(
        name='iron longsword',
        tier=10,
        attack_speed=3,
        stats=Stats({
            'physical_strength': 4,
            'magical_power': 1,
            'accuracy': 1,
        }),
    ),
    'steel longsword': Weapon(
        name='steel longsword',
        tier=15,
        attack_speed=3,
        stats=Stats({
            'physical_strength': 6,
            'magical_power': 1,
            'accuracy': 1,
        }),
    ),
    'mithril longsword': Weapon(
        name='mithril longsword',
        tier=20,
        attack_speed=3,
        stats=Stats({
            'physical_strength': 8,
            'magical_power': 1,
            'accuracy': 1,
        }),
    ),
    'adamant longsword': Weapon(
        name='adamant longsword',
        tier=30,
        attack_speed=3,
        stats=Stats({
            'physical_strength': 11,
            'magical_power': 2,
            'accuracy': 2,
        }),
    ),
    'rune longsword': Weapon(
        name='rune longsword',
        tier=40,
        attack_speed=3,
        stats=Stats({
            'physical_strength': 14,
            'magical_power': 3,
            'accuracy': 3,
        }),
    ),
    'orikalkum longsword': Weapon(
        name='orikalkum longsword',
        tier=60,
        attack_speed=3,
        stats=Stats({
            'physical_strength': 20,
            'magical_power': 4,
            'accuracy': 4,
        }),
    ),
    'necronium longsword': Weapon(
        name='necronium longsword',
        tier=70,
        attack_speed=3,
        stats=Stats({
            'physical_strength': 24,
            'magical_power': 5,
            'accuracy': 5,
        }),
    ),
    'bane longsword': Weapon(
        name='bane longsword',
        tier=80,
        attack_speed=3,
        stats=Stats({
            'physical_strength': 27,
            'magical_power': 5,
            'accuracy': 5,
        }),
    ),
    'elder longsword': Weapon(
        name='elder longsword',
        tier=90,
        attack_speed=3,
        stats=Stats({
            'physical_strength': 30,
            'magical_power': 6,
            'accuracy': 6,
        }),
    ),
}
