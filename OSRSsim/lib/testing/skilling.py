from ...util.structures import Player


def testing_skilling(player: Player):
    items = {
        'Iron pickaxe': 1,
        'Iron ore': 2,
    }

    player.give(items)
