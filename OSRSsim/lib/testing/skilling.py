from ...util.structures import Player


def testing_skilling(player: Player):
    items = {
        'Iron pickaxe': 1,
        'Iron axe': 1,
    }

    player.give(items)
