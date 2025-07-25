from ....util.structures.Produceable import Produceable


class Smeltable(Produceable):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


smeltables = {
    'copper': Smeltable(
        name='copper bar',
        XP=6.,
        level=1,
        ticks_per_action=3,
        items_required={
            'copper ore': 2,
        },
    ),
    'iron': Smeltable(
        name='iron bar',
        XP=12.5,
        level=1,
        ticks_per_action=3,
        items_required={
            'iron ore': 2,
        },
    ),
    'steel': Smeltable(
        name='steel bar',
        XP=17.5,
        level=1,
        ticks_per_action=3,
        items_required={
            'iron ore': 1,
            'coal': 1,
        },
    ),
    'mithril': Smeltable(
        name='mithril bar',
        XP=30.,
        level=1,
        ticks_per_action=3,
        items_required={
            'mithril ore': 2,
        },
    ),
    'adamant': Smeltable(
        name='adamantite bar',
        XP=37.5,
        level=1,
        ticks_per_action=3,
        items_required={
            'adamantite ore': 2,
        },
    ),
    'rune': Smeltable(
        name='runite bar',
        XP=50.,
        level=1,
        ticks_per_action=3,
        items_required={
            'runite ore': 2,
        },
    ),
}
