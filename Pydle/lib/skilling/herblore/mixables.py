from ....util.structures.Produceable import Produceable


class Mixable(Produceable):

    def __init__(self, n_doses: int = 1, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.n_doses: int = n_doses


MIXABLES = {
    'attack': Mixable(
        name='attack potion',
        n_doses=3,
        level=1,
        xp=25.,
        items_required={
            'vial': 3,
            'guam': 1,
            'eye of newt': 1,
        },
        ticks_per_action=5,
    ),
}
