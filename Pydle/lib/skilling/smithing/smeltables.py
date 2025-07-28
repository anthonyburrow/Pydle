from ....util.structures.Produceable import Produceable


class Smeltable(Produceable):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


SMELTABLES = {
    'copper': Smeltable(
        name='copper bar',
        xp=2.,
        level=1,
        ticks_per_action=3,
        items_required={
            'copper ore': 2,
        },
    ),
    'silver': Smeltable(
        name='silver bar',
        xp=3.,
        level=5,
        ticks_per_action=3,
        items_required={
            'silver ore': 2,
        },
    ),
    'iron': Smeltable(
        name='iron bar',
        xp=5.,
        level=10,
        ticks_per_action=3,
        items_required={
            'iron ore': 2,
        },
    ),
    'steel': Smeltable(
        name='steel bar',
        xp=9.,
        level=15,
        ticks_per_action=3,
        items_required={
            'iron ore': 2,
            'coal': 1,
        },
    ),
    'gold': Smeltable(
        name='gold bar',
        xp=14.,
        level=20,
        ticks_per_action=3,
        items_required={
            'gold ore': 2,
        },
    ),
    'adamantite': Smeltable(
        name='adamantite bar',
        xp=26.,
        level=30,
        ticks_per_action=3,
        items_required={
            'adamantite ore': 2,
            'coal': 1,
        },
    ),
    'blackirn': Smeltable(
        name='blackirn bar',
        xp=40.,
        level=50,
        ticks_per_action=3,
        items_required={
            'black ore': 2,
        },
    ),
    'wyrmheart': Smeltable(
        name='wyrmheart bar',
        xp=60.,
        level=70,
        ticks_per_action=3,
        items_required={
            'wyrmheart ore': 2,
        },
    ),
    'valnorite': Smeltable(
        name='valnorite bar',
        xp=100.,
        level=90,
        ticks_per_action=3,
        items_required={
            'valnorite ore': 2,
        },
    ),
    'kharadant': Smeltable(
        name='kharadant bar',
        xp=160.,
        level=110,
        ticks_per_action=3,
        items_required={
            'kharad ore': 2,
        },
    ),
}
