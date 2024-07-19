from ...util.structures import Player


def testing_skilling(player: Player):
    items = {
        'copper pickaxe': 1,
        'iron pickaxe': 1,
        'iron axe': 1,
        'iron secateurs': 1,
    }

    player.give(items)
