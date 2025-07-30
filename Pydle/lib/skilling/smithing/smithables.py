from ....util.structures.Produceable import Produceable


class Smithable(Produceable):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)



SMITHABLES = {
    #
    # Copper
    #
    'copper longsword': Smithable(
        name='copper longsword',
        xp=16.,
        level=1,
        ticks_per_action=6,
        items_required={
            'copper bar': 2,
        },
    ),
    'copper kiteshield': Smithable(
        name='copper kiteshield',
        xp=16.,
        level=1,
        ticks_per_action=6,
        items_required={
            'copper bar': 2,
        },
    ),
    'copper helm': Smithable(
        name='copper helm',
        xp=16.,
        level=1,
        ticks_per_action=6,
        items_required={
            'copper bar': 2,
        },
    ),
    'copper chestplate': Smithable(
        name='copper chestplate',
        xp=24.,
        level=1,
        ticks_per_action=6,
        items_required={
            'copper bar': 3,
        },
    ),
    'copper platelegs': Smithable(
        name='copper platelegs',
        xp=24.,
        level=1,
        ticks_per_action=6,
        items_required={
            'copper bar': 3,
        },
    ),
    'copper gauntlets': Smithable(
        name='copper gauntlets',
        xp=8.,
        level=1,
        ticks_per_action=6,
        items_required={
            'copper bar': 1,
        },
    ),
    'copper boots': Smithable(
        name='copper boots',
        xp=8.,
        level=1,
        ticks_per_action=6,
        items_required={
            'copper bar': 1,
        },
    ),
    'copper pickaxe': Smithable(
        name='copper pickaxe',
        xp=24.,
        level=1,
        ticks_per_action=6,
        items_required={
            'copper bar': 3,
            'pine log': 1,
        },
    ),
    'copper axe': Smithable(
        name='copper axe',
        xp=16.,
        level=1,
        ticks_per_action=6,
        items_required={
            'copper bar': 2,
            'pine log': 1,
        },
    ),
    #
    # Iron
    #
    'iron longsword': Smithable(
        name='iron longsword',
        xp=40.,
        level=10,
        ticks_per_action=6,
        items_required={
            'iron bar': 2,
        },
    ),
    'iron kiteshield': Smithable(
        name='iron kiteshield',
        xp=40.,
        level=10,
        ticks_per_action=6,
        items_required={
            'iron bar': 2,
        },
    ),
    'iron helm': Smithable(
        name='iron helm',
        xp=40.,
        level=10,
        ticks_per_action=6,
        items_required={
            'iron bar': 2,
        },
    ),
    'iron chestplate': Smithable(
        name='iron chestplate',
        xp=60.,
        level=10,
        ticks_per_action=6,
        items_required={
            'iron bar': 3,
        },
    ),
    'iron platelegs': Smithable(
        name='iron platelegs',
        xp=60.,
        level=10,
        ticks_per_action=6,
        items_required={
            'iron bar': 3,
        },
    ),
    'iron gauntlets': Smithable(
        name='iron gauntlets',
        xp=20.,
        level=10,
        ticks_per_action=6,
        items_required={
            'iron bar': 1,
        },
    ),
    'iron boots': Smithable(
        name='iron boots',
        xp=20.,
        level=10,
        ticks_per_action=6,
        items_required={
            'iron bar': 1,
        },
    ),
    'iron pickaxe': Smithable(
        name='iron pickaxe',
        xp=60.,
        level=10,
        ticks_per_action=6,
        items_required={
            'iron bar': 3,
            'birch log': 1,
        },
    ),
    'iron axe': Smithable(
        name='iron axe',
        xp=40.,
        level=10,
        ticks_per_action=6,
        items_required={
            'iron bar': 2,
            'birch log': 1,
        },
    ),
    #
    # Steel
    #
    'steel longsword': Smithable(
        name='steel longsword',
        xp=72.,
        level=15,
        ticks_per_action=6,
        items_required={
            'steel bar': 2,
        },
    ),
    'steel kiteshield': Smithable(
        name='steel kiteshield',
        xp=72.,
        level=15,
        ticks_per_action=6,
        items_required={
            'steel bar': 2,
        },
    ),
    'steel helm': Smithable(
        name='steel helm',
        xp=72.,
        level=15,
        ticks_per_action=6,
        items_required={
            'steel bar': 2,
        },
    ),
    'steel chestplate': Smithable(
        name='steel chestplate',
        xp=108.,
        level=15,
        ticks_per_action=6,
        items_required={
            'steel bar': 3,
        },
    ),
    'steel platelegs': Smithable(
        name='steel platelegs',
        xp=108.,
        level=15,
        ticks_per_action=6,
        items_required={
            'steel bar': 3,
        },
    ),
    'steel gauntlets': Smithable(
        name='steel gauntlets',
        xp=36.,
        level=15,
        ticks_per_action=6,
        items_required={
            'steel bar': 1,
        },
    ),
    'steel boots': Smithable(
        name='steel boots',
        xp=36.,
        level=15,
        ticks_per_action=6,
        items_required={
            'steel bar': 1,
        },
    ),
    'steel pickaxe': Smithable(
        name='steel pickaxe',
        xp=108.,
        level=15,
        ticks_per_action=6,
        items_required={
            'steel bar': 3,
            'maple log': 1,
        },
    ),
    'steel axe': Smithable(
        name='steel axe',
        xp=72.,
        level=15,
        ticks_per_action=6,
        items_required={
            'steel bar': 2,
            'maple log': 1,
        },
    ),
    #
    # Adamant
    #
    'adamant longsword': Smithable(
        name='adamant longsword',
        xp=208.,
        level=30,
        ticks_per_action=6,
        items_required={
            'adamantite bar': 2,
        },
    ),
    'adamant kiteshield': Smithable(
        name='adamant kiteshield',
        xp=208.,
        level=30,
        ticks_per_action=6,
        items_required={
            'adamantite bar': 2,
        },
    ),
    'adamant helm': Smithable(
        name='adamant helm',
        xp=208.,
        level=30,
        ticks_per_action=6,
        items_required={
            'adamantite bar': 2,
        },
    ),
    'adamant chestplate': Smithable(
        name='adamant chestplate',
        xp=312.,
        level=30,
        ticks_per_action=6,
        items_required={
            'adamantite bar': 3,
        },
    ),
    'adamant platelegs': Smithable(
        name='adamant platelegs',
        xp=312.,
        level=30,
        ticks_per_action=6,
        items_required={
            'adamantite bar': 3,
        },
    ),
    'adamant gauntlets': Smithable(
        name='adamant gauntlets',
        xp=104.,
        level=30,
        ticks_per_action=6,
        items_required={
            'adamantite bar': 1,
        },
    ),
    'adamant boots': Smithable(
        name='adamant boots',
        xp=104.,
        level=30,
        ticks_per_action=6,
        items_required={
            'adamantite bar': 1,
        },
    ),
    'adamant pickaxe': Smithable(
        name='adamant pickaxe',
        xp=312.,
        level=30,
        ticks_per_action=6,
        items_required={
            'adamantite bar': 3,
            'oak log': 1,
        },
    ),
    'adamant axe': Smithable(
        name='adamant axe',
        xp=208.,
        level=30,
        ticks_per_action=6,
        items_required={
            'adamantite bar': 2,
            'oak log': 1,
        },
    ),
}
