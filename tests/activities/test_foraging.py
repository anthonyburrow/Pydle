from Pydle.commands.Command import Command
from Pydle.commands.Activity import ActivityCheckResult
from Pydle.commands.activities.skilling.foraging import ForagingActivity
from Pydle.util.items.ItemInstance import ItemInstance
from Pydle.util.items.ItemParser import ITEM_PARSER
from Pydle.util.player.SkillType import SkillType


def test_no_collectables_in_area(test_player, test_ui) -> None:
    test_player.set_level(SkillType.FORAGING, 99)
    test_player.set_area('eastveil')

    raw_in: str = 'collect'
    command: Command = Command(raw_in)

    secateurs: ItemInstance = ITEM_PARSER.get_instance('poor copper secateurs')
    test_player.give(secateurs)
    test_player.equip_tool(secateurs)

    activity: ForagingActivity = ForagingActivity(test_player, test_ui, command)
    result_check: ActivityCheckResult = activity.check()
    assert not result_check.success


# def test_low_level_for_all_items(test_player, test_ui) -> None:
#     test_player.set_level(SkillType.FORAGING, 1)

#     raw_in: str = 'collect'
#     command: Command = Command(raw_in)

#     secateurs: ItemInstance = ITEM_PARSER.get_instance('poor copper secateurs')
#     test_player.give(secateurs)
#     test_player.equip_tool(secateurs)

#     activity: ForagingActivity = ForagingActivity(test_player, test_ui, command)
#     result_check: ActivityCheckResult = activity.check()
#     assert not result_check.success


def test_missing_secateurs(test_player, test_ui) -> None:
    test_player.set_level(SkillType.FORAGING, 99)

    raw_in: str = 'collect'
    command: Command = Command(raw_in)

    activity: ForagingActivity = ForagingActivity(test_player, test_ui, command)
    result_check: ActivityCheckResult = activity.check()
    assert not result_check.success


def test_check_passes_with_all_requirements(test_player, test_ui) -> None:
    test_player.set_level(SkillType.FORAGING, 99)

    raw_in: str = 'collect'
    command: Command = Command(raw_in)

    secateurs: ItemInstance = ITEM_PARSER.get_instance('poor copper secateurs')
    test_player.give(secateurs)
    test_player.equip_tool(secateurs)

    activity: ForagingActivity = ForagingActivity(test_player, test_ui, command)
    result_check: ActivityCheckResult = activity.check()
    assert result_check.success
