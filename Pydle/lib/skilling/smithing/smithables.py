from ....util.structures.Produceable import Produceable


class Smithable(Produceable):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)



smithables = {
    #
    # Copper
    #
    'copper longsword': Smithable(
        name='copper longsword',
        xp=25.,
        level=1,
        ticks_per_action=6,
        items_required={
            'copper bar': 2,
        },
    ),
    'copper kiteshield': Smithable(
        name='copper kiteshield',
        xp=25.,
        level=1,
        ticks_per_action=6,
        items_required={
            'copper bar': 2,
        },
    ),
    'copper helm': Smithable(
        name='copper helm',
        xp=25.,
        level=1,
        ticks_per_action=6,
        items_required={
            'copper bar': 2,
        },
    ),
    'copper chestplate': Smithable(
        name='copper chestplate',
        xp=37.5,
        level=1,
        ticks_per_action=6,
        items_required={
            'copper bar': 3,
        },
    ),
    'copper platelegs': Smithable(
        name='copper platelegs',
        xp=37.5,
        level=1,
        ticks_per_action=6,
        items_required={
            'copper bar': 3,
        },
    ),
    'copper gauntlets': Smithable(
        name='copper gauntlets',
        xp=12.5,
        level=1,
        ticks_per_action=6,
        items_required={
            'copper bar': 1,
        },
    ),
    'copper boots': Smithable(
        name='copper boots',
        xp=12.5,
        level=1,
        ticks_per_action=6,
        items_required={
            'copper bar': 1,
        },
    ),
    #
    # Iron
    #
    'iron longsword': Smithable(
        name='iron longsword',
        xp=50.,
        level=10,
        ticks_per_action=6,
        items_required={
            'iron bar': 2,
        },
    ),
    'iron kiteshield': Smithable(
        name='iron kiteshield',
        xp=50.,
        level=10,
        ticks_per_action=6,
        items_required={
            'iron bar': 2,
        },
    ),
    'iron helm': Smithable(
        name='iron helm',
        xp=50.,
        level=10,
        ticks_per_action=6,
        items_required={
            'iron bar': 2,
        },
    ),
    'iron chestplate': Smithable(
        name='iron chestplate',
        xp=75.,
        level=10,
        ticks_per_action=6,
        items_required={
            'iron bar': 3,
        },
    ),
    'iron platelegs': Smithable(
        name='iron platelegs',
        xp=75.,
        level=10,
        ticks_per_action=6,
        items_required={
            'iron bar': 3,
        },
    ),
    'iron gauntlets': Smithable(
        name='iron gauntlets',
        xp=25.,
        level=10,
        ticks_per_action=6,
        items_required={
            'iron bar': 1,
        },
    ),
    'iron boots': Smithable(
        name='iron boots',
        xp=25.,
        level=10,
        ticks_per_action=6,
        items_required={
            'iron bar': 1,
        },
    ),
    #
    # Steel
    #
    'steel longsword': Smithable(
        name='steel longsword',
        xp=75.,
        level=15,
        ticks_per_action=6,
        items_required={
            'steel bar': 2,
        },
    ),
    'steel kiteshield': Smithable(
        name='steel kiteshield',
        xp=75.,
        level=15,
        ticks_per_action=6,
        items_required={
            'steel bar': 2,
        },
    ),
    'steel helm': Smithable(
        name='steel helm',
        xp=75.,
        level=15,
        ticks_per_action=6,
        items_required={
            'steel bar': 2,
        },
    ),
    'steel chestplate': Smithable(
        name='steel chestplate',
        xp=112.5,
        level=15,
        ticks_per_action=6,
        items_required={
            'steel bar': 3,
        },
    ),
    'steel platelegs': Smithable(
        name='steel platelegs',
        xp=112.5,
        level=15,
        ticks_per_action=6,
        items_required={
            'steel bar': 3,
        },
    ),
    'steel gauntlets': Smithable(
        name='steel gauntlets',
        xp=37.5,
        level=15,
        ticks_per_action=6,
        items_required={
            'steel bar': 1,
        },
    ),
    'steel boots': Smithable(
        name='steel boots',
        xp=37.5,
        level=15,
        ticks_per_action=6,
        items_required={
            'steel bar': 1,
        },
    ),
    #
    # Mithril
    #
    'mithril longsword': Smithable(
        name='mithril longsword',
        xp=100.,
        level=20,
        ticks_per_action=6,
        items_required={
            'mithril bar': 2,
        },
    ),
    'mithril kiteshield': Smithable(
        name='mithril kiteshield',
        xp=100.,
        level=20,
        ticks_per_action=6,
        items_required={
            'mithril bar': 2,
        },
    ),
    'mithril helm': Smithable(
        name='mithril helm',
        xp=100.,
        level=20,
        ticks_per_action=6,
        items_required={
            'mithril bar': 2,
        },
    ),
    'mithril chestplate': Smithable(
        name='mithril chestplate',
        xp=150.,
        level=20,
        ticks_per_action=6,
        items_required={
            'mithril bar': 3,
        },
    ),
    'mithril platelegs': Smithable(
        name='mithril platelegs',
        xp=150.,
        level=20,
        ticks_per_action=6,
        items_required={
            'mithril bar': 3,
        },
    ),
    'mithril gauntlets': Smithable(
        name='mithril gauntlets',
        xp=50.,
        level=20,
        ticks_per_action=6,
        items_required={
            'mithril bar': 1,
        },
    ),
    'mithril boots': Smithable(
        name='mithril boots',
        xp=50.,
        level=20,
        ticks_per_action=6,
        items_required={
            'mithril bar': 1,
        },
    ),
    #
    # Adamant
    #
    'adamant longsword': Smithable(
        name='adamant longsword',
        xp=125.,
        level=30,
        ticks_per_action=6,
        items_required={
            'adamantite bar': 2,
        },
    ),
    'adamant kiteshield': Smithable(
        name='adamant kiteshield',
        xp=125.,
        level=30,
        ticks_per_action=6,
        items_required={
            'adamantite bar': 2,
        },
    ),
    'adamant helm': Smithable(
        name='adamant helm',
        xp=125.,
        level=30,
        ticks_per_action=6,
        items_required={
            'adamantite bar': 2,
        },
    ),
    'adamant chestplate': Smithable(
        name='adamant chestplate',
        xp=187.5,
        level=30,
        ticks_per_action=6,
        items_required={
            'adamantite bar': 3,
        },
    ),
    'adamant platelegs': Smithable(
        name='adamant platelegs',
        xp=187.5,
        level=30,
        ticks_per_action=6,
        items_required={
            'adamantite bar': 3,
        },
    ),
    'adamant gauntlets': Smithable(
        name='adamant gauntlets',
        xp=62.5,
        level=30,
        ticks_per_action=6,
        items_required={
            'adamantite bar': 1,
        },
    ),
    'adamant boots': Smithable(
        name='adamant boots',
        xp=62.5,
        level=30,
        ticks_per_action=6,
        items_required={
            'adamantite bar': 1,
        },
    ),
    #
    # Rune
    #
    'rune longsword': Smithable(
        name='rune longsword',
        xp=150.,
        level=40,
        ticks_per_action=6,
        items_required={
            'runite bar': 2,
        },
    ),
    'rune kiteshield': Smithable(
        name='rune kiteshield',
        xp=150.,
        level=40,
        ticks_per_action=6,
        items_required={
            'runite bar': 2,
        },
    ),
    'rune helm': Smithable(
        name='rune helm',
        xp=150.,
        level=40,
        ticks_per_action=6,
        items_required={
            'runite bar': 2,
        },
    ),
    'rune chestplate': Smithable(
        name='rune chestplate',
        xp=225.,
        level=40,
        ticks_per_action=6,
        items_required={
            'runite bar': 3,
        },
    ),
    'rune platelegs': Smithable(
        name='rune platelegs',
        xp=225.,
        level=40,
        ticks_per_action=6,
        items_required={
            'runite bar': 3,
        },
    ),
    'rune gauntlets': Smithable(
        name='rune gauntlets',
        xp=75.,
        level=40,
        ticks_per_action=6,
        items_required={
            'runite bar': 1,
        },
    ),
    'rune boots': Smithable(
        name='rune boots',
        xp=75.,
        level=40,
        ticks_per_action=6,
        items_required={
            'runite bar': 1,
        },
    ),
}
