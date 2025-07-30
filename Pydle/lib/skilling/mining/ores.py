from ....util.structures.Gatherable import Gatherable


class Ore(Gatherable):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


ORES = {
    'copper': Ore(
        name='copper ore',
        xp=5.,
        level=1,
    ),
    'silver': Ore(
        name='silver ore',
        xp=7.5,
        level=5,
    ),
    'iron': Ore(
        name='iron ore',
        xp=12.5,
        level=10,
    ),
    'coal': Ore(
        name='coal',
        xp=20.,
        level=15,
    ),
    'gold': Ore(
        name='gold ore',
        xp=35.,
        level=20,
    ),
    'adamantite': Ore(
        name='adamantite ore',
        xp=55.,
        level=30,
    ),
    'hexstone': Ore(
        name='hexstone ore',
        xp=75.,
        level=40,
    ),
    'black': Ore(
        name='black ore',
        xp=100.,
        level=50,
    ),
    'witchsilver': Ore(
        name='witchsilver ore',
        xp=125.,
        level=60,
    ),
    'wyrmheart': Ore(
        name='wyrmheart ore',
        xp=150.,
        level=70,
    ),
    'veilstone': Ore(
        name='veilstone ore',
        xp=200.,
        level=80,
    ),
    'valnorite': Ore(
        name='valnorite ore',
        xp=250.,
        level=90,
    ),
    'cursevein': Ore(
        name='cursevein ore',
        xp=325.,
        level=100,
    ),
    'kharad': Ore(
        name='kharad ore',
        xp=400.,
        level=110,
    ),
    'voidcrystal': Ore(
        name='voidcrystal shard',
        xp=475.,
        level=120,
    ),
}
