from ....util.structures.Gatherable import Gatherable


class Log(Gatherable):

    def __init__(self, ticks_per_fire, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.ticks_per_fire: int = ticks_per_fire


logs = {
    'logs': Log(
        name='logs',
        xp=12.5,
        level=1,
        ticks_per_fire=30,
        gather_value=1.00,
    ),
    'oak': Log(
        name='oak logs',
        xp=22.5,
        level=10,
        ticks_per_fire=30,
        gather_value=0.83,
    ),
    'willow': Log(
        name='willow logs',
        xp=35.,
        level=15,
        ticks_per_fire=30,
        gather_value=0.69,
    ),
    'teak': Log(
        name='teak logs',
        xp=50.,
        level=20,
        ticks_per_fire=30,
        gather_value=0.56,
    ),
    'maple': Log(
        name='maple logs',
        xp=65.,
        level=30,
        ticks_per_fire=30,
        gather_value=0.46,
    ),
    'acadia': Log(
        name='acadia logs',
        xp=85.,
        level=40,
        ticks_per_fire=30,
        gather_value=0.37,
    ),
    'mahogany': Log(
        name='mahogany logs',
        xp=125.,
        level=60,
        ticks_per_fire=30,
        gather_value=0.29,
    ),
    'yew': Log(
        name='yew logs',
        xp=175.,
        level=70,
        ticks_per_fire=30,
        gather_value=0.22,
    ),
    'magic': Log(
        name='magic logs',
        xp=240.,
        level=80,
        ticks_per_fire=30,
        gather_value=0.16,
    ),
    'elder': Log(
        name='elder logs',
        xp=350.,
        level=90,
        ticks_per_fire=30,
        gather_value=0.11,
    ),

}
