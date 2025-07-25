from ....util.structures.Gatherable import Gatherable


class Herb(Gatherable):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


herbs = {
    'guam': Herb(
        name='grimy guam',
        level=1,
        XP=12.5,
        gather_value=1.00,
    ),
    'marrentill': Herb(
        name='grimy marrentill',
        level=10,
        XP=22.5,
        gather_value=0.83,
    ),
    'harralander': Herb(
        name='grimy harralander',
        level=15,
        XP=35.,
        gather_value=0.69,
    ),
    'ranarr': Herb(
        name='grimy ranarr',
        level=20,
        XP=50.,
        gather_value=0.56,
    ),
    'toadflax': Herb(
        name='grimy toadflax',
        level=30,
        XP=65.,
        gather_value=0.46,
    ),
    'irit': Herb(
        name='grimy irit',
        level=40,
        XP=85.,
        gather_value=0.37,
    ),
    'kwuarm': Herb(
        name='grimy avantoe',
        level=60,
        XP=125.,
        gather_value=0.29,
    ),
    'snapdragon': Herb(
        name='grimy snapdragon',
        level=70,
        XP=175.,
        gather_value=0.22,
    ),
    'torstol': Herb(
        name='grimy torstol',
        level=80,
        XP=240.,
        gather_value=0.16,
    ),
    'fellstalk': Herb(
        name='grimy fellstalk',
        level=90,
        XP=350.,
        gather_value=0.11,
    ),
}
