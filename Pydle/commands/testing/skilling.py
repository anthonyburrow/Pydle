from ...util.player.Bank import Bank
from ...util.player.Player import Player


def testing_skilling(player: Player):
    items: Bank = Bank.from_dict({
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
    })

    player.give(items)
