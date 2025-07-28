from ...util.structures.Equippable import Weapon
from ...util.structures.Stats import Stats


WEAPONS = {
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
            'magical_power': 0,
            'accuracy': 1,
        }),
    ),
    'steel longsword': Weapon(
        name='steel longsword',
        tier=15,
        attack_speed=3,
        stats=Stats({
            'physical_strength': 6,
            'magical_power': 0,
            'accuracy': 1,
        }),
    ),
    'adamant longsword': Weapon(
        name='adamant longsword',
        tier=30,
        attack_speed=3,
        stats=Stats({
            'physical_strength': 11,
            'magical_power': 0,
            'accuracy': 2,
        }),
    ),
}
