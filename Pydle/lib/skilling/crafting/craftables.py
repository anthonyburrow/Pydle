from ....util.structures.Produceable import Produceable


class Craftable(Produceable):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


CRAFTABLES = {
    'leather': Craftable(
        name='leather',
        level=1,
        xp=6.,
        items_required={
            'raw hide': 1,
        },
        ticks_per_action=2,
    ),
    'leather gloves': Craftable(
        name='leather gloves',
        level=1,
        xp=15.,
        items_required={
            'leather': 1,
        },
        ticks_per_action=5,
    ),
}
