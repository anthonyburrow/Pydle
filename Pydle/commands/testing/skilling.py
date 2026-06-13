from ...util.items.ItemParser import ITEM_PARSER
from ...util.player.Bank import Bank
from ...util.player.Player import Player


def testing_skilling(player: Player):
    items = (Bank()
        .add(ITEM_PARSER.get_instance('copper pickaxe', 1))
        .add(ITEM_PARSER.get_instance('iron pickaxe', 1))
        .add(ITEM_PARSER.get_instance('iron axe', 1))
        .add(ITEM_PARSER.get_instance('iron secateurs', 1))
        .add(ITEM_PARSER.get_instance('copper fishing rod', 1))
        .add(ITEM_PARSER.get_instance('iron fishing rod', 1))
        .add(ITEM_PARSER.get_instance('copper helm', 1))
        .add(ITEM_PARSER.get_instance('vial', 1000))
        .add(ITEM_PARSER.get_instance('eye of newt', 1000))
        .add(ITEM_PARSER.get_instance('raw hide', 1000))
    )

    player.give(items)
