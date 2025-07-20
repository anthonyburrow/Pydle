from ..Gatherable import Gatherable


class Ore(Gatherable):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


ores = {
    'copper': Ore(
        name='copper ore',
        XP=12.5,
        level=1,
        gather_value=1.00,
    ),
    'iron': Ore(
        name='iron ore',
        XP=22.5,
        level=10,
        gather_value=0.83,
    ),
    'coal': Ore(
        name='coal',
        XP=35.,
        level=15,
        gather_value=0.69,
    ),
    'mithril': Ore(
        name='mithril ore',
        XP=50.,
        level=20,
        gather_value=0.56,
    ),
    'adamant': Ore(
        name='adamantite ore',
        XP=65.,
        level=30,
        gather_value=0.46,
    ),
    'rune': Ore(
        name='runite ore',
        XP=85.,
        level=40,
        gather_value=0.37,
    ),
    'orikalkum': Ore(
        name='orikalkum ore',
        XP=125.,
        level=60,
        gather_value=0.29,
    ),
    'necronium': Ore(
        name='necronium ore',
        XP=175.,
        level=70,
        gather_value=0.22,
    ),
    'bane': Ore(
        name='banite ore',
        XP=240.,
        level=80,
        gather_value=0.16,
    ),
    'elder': Ore(
        name='elder ore',
        XP=350.,
        level=90,
        gather_value=0.11,
    ),

}
