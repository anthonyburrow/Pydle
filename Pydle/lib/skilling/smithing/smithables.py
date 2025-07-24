
class Smithable:

    def __init__(
        self,
        name: str,
        XP: float,
        level: int,
        ticks_per_action: int,
        items_required: dict,
    ):
        self.name: str = name
        self.XP: float = XP
        self.level: int = level
        self.ticks_per_action: int = ticks_per_action
        self.items_required: dict = items_required


smithables = {
    #
    # Copper
    #
    'copper longsword': Smithable(
        name='copper longsword',
        XP=25.,
        level=1,
        ticks_per_action=6,
        items_required={
            'copper bar': 2,
        },
    ),
    'copper helm': Smithable(
        name='copper helm',
        XP=25.,
        level=1,
        ticks_per_action=6,
        items_required={
            'copper bar': 2,
        },
    ),
    'copper chestplate': Smithable(
        name='copper chestplate',
        XP=37.5,
        level=1,
        ticks_per_action=6,
        items_required={
            'copper bar': 3,
        },
    ),
    'copper platelegs': Smithable(
        name='copper platelegs',
        XP=37.5,
        level=1,
        ticks_per_action=6,
        items_required={
            'copper bar': 3,
        },
    ),
    'copper gauntlets': Smithable(
        name='copper gauntlets',
        XP=12.5,
        level=1,
        ticks_per_action=6,
        items_required={
            'copper bar': 1,
        },
    ),
    'copper boots': Smithable(
        name='copper boots',
        XP=12.5,
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
        XP=50.,
        level=10,
        ticks_per_action=6,
        items_required={
            'iron bar': 2,
        },
    ),
    'iron helm': Smithable(
        name='iron helm',
        XP=50.,
        level=10,
        ticks_per_action=6,
        items_required={
            'iron bar': 2,
        },
    ),
    'iron chestplate': Smithable(
        name='iron chestplate',
        XP=75.,
        level=10,
        ticks_per_action=6,
        items_required={
            'iron bar': 3,
        },
    ),
    'iron platelegs': Smithable(
        name='iron platelegs',
        XP=75.,
        level=10,
        ticks_per_action=6,
        items_required={
            'iron bar': 3,
        },
    ),
    'iron gauntlets': Smithable(
        name='iron gauntlets',
        XP=25.,
        level=10,
        ticks_per_action=6,
        items_required={
            'iron bar': 1,
        },
    ),
    'iron boots': Smithable(
        name='iron boots',
        XP=25.,
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
        XP=75.,
        level=15,
        ticks_per_action=6,
        items_required={
            'steel bar': 2,
        },
    ),
    'steel helm': Smithable(
        name='steel helm',
        XP=75.,
        level=15,
        ticks_per_action=6,
        items_required={
            'steel bar': 2,
        },
    ),
    'steel chestplate': Smithable(
        name='steel chestplate',
        XP=112.5,
        level=15,
        ticks_per_action=6,
        items_required={
            'steel bar': 3,
        },
    ),
    'steel platelegs': Smithable(
        name='steel platelegs',
        XP=112.5,
        level=15,
        ticks_per_action=6,
        items_required={
            'steel bar': 3,
        },
    ),
    'steel gauntlets': Smithable(
        name='steel gauntlets',
        XP=37.5,
        level=15,
        ticks_per_action=6,
        items_required={
            'steel bar': 1,
        },
    ),
    'steel boots': Smithable(
        name='steel boots',
        XP=37.5,
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
        XP=100.,
        level=20,
        ticks_per_action=6,
        items_required={
            'mithril bar': 2,
        },
    ),
    'mithril helm': Smithable(
        name='mithril helm',
        XP=100.,
        level=20,
        ticks_per_action=6,
        items_required={
            'mithril bar': 2,
        },
    ),
    'mithril chestplate': Smithable(
        name='mithril chestplate',
        XP=150.,
        level=20,
        ticks_per_action=6,
        items_required={
            'mithril bar': 3,
        },
    ),
    'mithril platelegs': Smithable(
        name='mithril platelegs',
        XP=150.,
        level=20,
        ticks_per_action=6,
        items_required={
            'mithril bar': 3,
        },
    ),
    'mithril gauntlets': Smithable(
        name='mithril gauntlets',
        XP=50.,
        level=20,
        ticks_per_action=6,
        items_required={
            'mithril bar': 1,
        },
    ),
    'mithril boots': Smithable(
        name='mithril boots',
        XP=50.,
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
        XP=125.,
        level=30,
        ticks_per_action=6,
        items_required={
            'adamantite bar': 2,
        },
    ),
    'adamant helm': Smithable(
        name='adamant helm',
        XP=125.,
        level=30,
        ticks_per_action=6,
        items_required={
            'adamantite bar': 2,
        },
    ),
    'adamant chestplate': Smithable(
        name='adamant chestplate',
        XP=187.5,
        level=30,
        ticks_per_action=6,
        items_required={
            'adamantite bar': 3,
        },
    ),
    'adamant platelegs': Smithable(
        name='adamant platelegs',
        XP=187.5,
        level=30,
        ticks_per_action=6,
        items_required={
            'adamantite bar': 3,
        },
    ),
    'adamant gauntlets': Smithable(
        name='adamant gauntlets',
        XP=62.5,
        level=30,
        ticks_per_action=6,
        items_required={
            'adamantite bar': 1,
        },
    ),
    'adamant boots': Smithable(
        name='adamant boots',
        XP=62.5,
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
        XP=150.,
        level=40,
        ticks_per_action=6,
        items_required={
            'runite bar': 2,
        },
    ),
    'rune helm': Smithable(
        name='rune helm',
        XP=150.,
        level=40,
        ticks_per_action=6,
        items_required={
            'runite bar': 2,
        },
    ),
    'rune chestplate': Smithable(
        name='rune chestplate',
        XP=225.,
        level=40,
        ticks_per_action=6,
        items_required={
            'runite bar': 3,
        },
    ),
    'rune platelegs': Smithable(
        name='rune platelegs',
        XP=225.,
        level=40,
        ticks_per_action=6,
        items_required={
            'runite bar': 3,
        },
    ),
    'rune gauntlets': Smithable(
        name='rune gauntlets',
        XP=75.,
        level=40,
        ticks_per_action=6,
        items_required={
            'runite bar': 1,
        },
    ),
    'rune boots': Smithable(
        name='rune boots',
        XP=75.,
        level=40,
        ticks_per_action=6,
        items_required={
            'runite bar': 1,
        },
    ),
}
