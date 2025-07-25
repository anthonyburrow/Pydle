from ....util.structures.Gatherable import Gatherable


class Ore(Gatherable):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


ores = {
    'copper': Ore(
        name='copper ore',
        xp=12.5,
        level=1,
        gather_value=0.90,
    ),
    'iron': Ore(
        name='iron ore',
        xp=17.5,
        level=10,
        gather_value=0.75,
    ),
    'coal': Ore(
        name='coal',
        xp=30.,
        level=15,
        gather_value=0.50,
    ),
    'mithril': Ore(
        name='mithril ore',
        xp=40.,
        level=20,
        gather_value=0.40,
    ),
    'adamant': Ore(
        name='adamantite ore',
        xp=55.,
        level=30,
        gather_value=0.33,
    ),
    'rune': Ore(
        name='runite ore',
        xp=70.,
        level=40,
        gather_value=0.28,
    ),
    'orikalkum': Ore(
        name='orikalkum ore',
        xp=100.,
        level=60,
        gather_value=0.21,
    ),
    'necronium': Ore(
        name='necronium ore',
        xp=135.,
        level=70,
        gather_value=0.17,
    ),
    'bane': Ore(
        name='banite ore',
        xp=180.,
        level=80,
        gather_value=0.14,
    ),
    'elder': Ore(
        name='elder ore',
        xp=250.,
        level=90,
        gather_value=0.11,
    ),

}
