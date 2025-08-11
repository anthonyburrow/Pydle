from Pydle.commands.activities.skilling.mining import MiningActivity
from Pydle.commands.Command import Command
from Pydle.util.items.ItemParser import ITEM_PARSER


def test_missing_pickaxe(test_player, test_ui):
    # Setup
    test_player.set_level('mining', 99)

    raw_in: str = 'mine copper ore'
    command: Command = Command(raw_in)

    # Test no pickaxe
    activity = MiningActivity(test_player, test_ui, command)
    result_check = activity.check()

    assert not result_check.success

    # Test has pickaxe
    test_player.give(ITEM_PARSER.get_instance('poor iron pickaxe'))
    test_player.equip_tool(ITEM_PARSER.get_instance('poor iron pickaxe'))

    activity = MiningActivity(test_player, test_ui, command)
    result_check = activity.check()

    assert result_check.success


def test_misspelled_ore(test_player, test_ui):
    # Setup
    test_player.set_level('mining', 99)

    raw_in: str = 'mine irn ore'
    command: Command = Command(raw_in)

    test_player.give(ITEM_PARSER.get_instance('poor iron pickaxe'))
    test_player.equip_tool(ITEM_PARSER.get_instance('poor iron pickaxe'))

    activity = MiningActivity(test_player, test_ui, command)
    result_check = activity.check()

    assert not result_check.success
