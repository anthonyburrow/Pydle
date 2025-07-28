from ....util.structures.Produceable import Produceable


class Cleanable(Produceable):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


CLEANABLES = {
    'guam': Cleanable(
        name='guam',
        level=1,
        xp=1.,
        items_required={
            'grimy guam': 1,
        },
        ticks_per_action=2,
    ),
    'marrentill': Cleanable(
        name='marrentill',
        level=10,
        xp=2.,
        items_required={
            'grimy marrentill': 1,
        },
        ticks_per_action=2,
    ),
    'harralander': Cleanable(
        name='harralander',
        level=15,
        xp=3.5,
        items_required={
            'grimy harralander': 1,
        },
        ticks_per_action=2,
    ),
    'ranarr': Cleanable(
        name='ranarr',
        level=20,
        xp=5.,
        items_required={
            'grimy ranarr': 1,
        },
        ticks_per_action=2,
    ),
    'toadflax': Cleanable(
        name='toadflax',
        level=30,
        xp=6.5,
        items_required={
            'grimy toadflax': 1,
        },
        ticks_per_action=2,
    ),
    'irit': Cleanable(
        name='irit',
        level=40,
        xp=8.5,
        items_required={
            'grimy irit': 1,
        },
        ticks_per_action=2,
    ),
    'kwuarm': Cleanable(
        name='kwuarm',
        level=50,
        xp=10.5,
        items_required={
            'grimy kwuarm': 1,
        },
        ticks_per_action=2,
    ),
    'avantoe': Cleanable(
        name='avantoe',
        level=60,
        xp=12.5,
        items_required={
            'grimy avantoe': 1,
        },
        ticks_per_action=2,
    ),
    'snapdragon': Cleanable(
        name='snapdragon',
        level=70,
        xp=17.5,
        items_required={
            'grimy snapdragon': 1,
        },
        ticks_per_action=2,
    ),
    'torstol': Cleanable(
        name='torstol',
        level=80,
        xp=24.,
        items_required={
            'grimy torstol': 1,
        },
        ticks_per_action=2,
    ),
    'fellstalk': Cleanable(
        name='fellstalk',
        level=90,
        xp=35.,
        items_required={
            'grimy fellstalk': 1,
        },
        ticks_per_action=2,
    ),
}
