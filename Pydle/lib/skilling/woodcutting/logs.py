from ....util.structures.Gatherable import Gatherable


class Log(Gatherable):

    def __init__(self, ticks_per_fire, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.ticks_per_fire: int = ticks_per_fire


LOGS = {
    'pine': Log(
        name='pine log',
        xp=5.,
        level=1,
        ticks_per_fire=30,
    ),
    'birch': Log(
        name='birch log',
        xp=12.5,
        level=10,
        ticks_per_fire=30,
    ),
    'maple': Log(
        name='maple log',
        xp=20.,
        level=15,
        ticks_per_fire=30,
    ),
    'willow': Log(
        name='willow log',
        xp=35.,
        level=20,
        ticks_per_fire=30,
    ),
    'oak': Log(
        name='oak log',
        xp=55.,
        level=30,
        ticks_per_fire=30,
    ),
    'elm': Log(
        name='elm log',
        xp=75.,
        level=40,
        ticks_per_fire=30,
    ),
    'yew': Log(
        name='yew log',
        xp=100.,
        level=50,
        ticks_per_fire=30,
    ),
    'bloodwood': Log(
        name='bloodwood log',
        xp=125.,
        level=60,
        ticks_per_fire=30,
    ),
    'ironwood': Log(
        name='ironwood log',
        xp=150.,
        level=70,
        ticks_per_fire=30,
    ),
    'ashen': Log(
        name='ashen log',
        xp=200.,
        level=80,
        ticks_per_fire=30,
    ),
    'heartwood': Log(
        name='heartwood log',
        xp=250.,
        level=90,
        ticks_per_fire=30,
    ),
    'glassthorn': Log(
        name='glassthorn log',
        xp=325.,
        level=100,
        ticks_per_fire=30,
    ),
    'emberpine': Log(
        name='emberpine log',
        xp=400.,
        level=110,
        ticks_per_fire=30,
    ),
    'ebonspire': Log(
        name='ebonspire log',
        xp=475.,
        level=120,
        ticks_per_fire=30,
    ),
}
