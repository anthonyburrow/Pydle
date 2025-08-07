from ..util.items.ItemParser import ITEM_PARSER
from ..util.player.Bank import Bank


NEW_PLAYER_ITEMS: Bank = Bank()

NEW_PLAYER_ITEMS.add(ITEM_PARSER.get_instance('copper pickaxe'))
NEW_PLAYER_ITEMS.add(ITEM_PARSER.get_instance('copper axe'))
NEW_PLAYER_ITEMS.add(ITEM_PARSER.get_instance('copper secateurs'))
NEW_PLAYER_ITEMS.add(ITEM_PARSER.get_instance('copper fishing rod'))
