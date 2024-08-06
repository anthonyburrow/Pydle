from ...util.structures.Player import Player


def testing_skilling(player: Player):
    items = {
        'copper pickaxe': 1,
        'iron pickaxe': 1,
        'iron axe': 1,
        'iron secateurs': 1,
        'copper fishing rod': 1,
        'iron fishing rod': 1,
        'copper helm': 1,
        'vial': 1000,
        'eye of newt': 1000,
        'raw hide': 1000,
    }

    player.give(items)
