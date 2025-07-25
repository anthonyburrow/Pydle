from ....util.structures.Produceable import Produceable


class Smeltable(Produceable):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


smeltables = {
    'copper': Smeltable(
        name='copper bar',
        xp=6.,
        level=1,
        ticks_per_action=3,
        items_required={
            'copper ore': 2,
        },
    ),
    'iron': Smeltable(
        name='iron bar',
        xp=12.5,
        level=1,
        ticks_per_action=3,
        items_required={
            'iron ore': 2,
        },
    ),
    'steel': Smeltable(
        name='steel bar',
        xp=17.5,
        level=1,
        ticks_per_action=3,
        items_required={
            'iron ore': 1,
            'coal': 1,
        },
    ),
    'mithril': Smeltable(
        name='mithril bar',
        xp=30.,
        level=1,
        ticks_per_action=3,
        items_required={
            'mithril ore': 2,
        },
    ),
    'adamant': Smeltable(
        name='adamantite bar',
        xp=37.5,
        level=1,
        ticks_per_action=3,
        items_required={
            'adamantite ore': 2,
        },
    ),
    'rune': Smeltable(
        name='runite bar',
        xp=50.,
        level=1,
        ticks_per_action=3,
        items_required={
            'runite ore': 2,
        },
    ),
}
