from Pydle.commands.Command import Command
from Pydle.commands.Activity import ActivityCheckResult
from Pydle.commands.activities.skilling.woodcutting import WoodcuttingActivity
from Pydle.util.items.ItemInstance import ItemInstance
from Pydle.util.items.ItemParser import ITEM_PARSER
from Pydle.util.player.SkillType import SkillType


def test_missing_axe(test_player, test_ui) -> None:
    test_player.set_level(SkillType.WOODCUTTING, 99)

    raw_in: str = 'chop pine log'
    command: Command = Command(raw_in)

    activity: WoodcuttingActivity = WoodcuttingActivity(test_player, test_ui, command)
    result_check: ActivityCheckResult = activity.check()
    assert not result_check.success

    axe: ItemInstance = ITEM_PARSER.get_instance('poor copper axe')
    test_player.give(axe)
    test_player.equip_tool(axe)

    activity = WoodcuttingActivity(test_player, test_ui, command)
    result_check = activity.check()
    assert result_check.success


def test_misspelled_log(test_player, test_ui) -> None:
    test_player.set_level(SkillType.WOODCUTTING, 99)

    raw_in: str = 'chop ok log'
    command: Command = Command(raw_in)

    axe: ItemInstance = ITEM_PARSER.get_instance('poor copper axe')
    test_player.give(axe)
    test_player.equip_tool(axe)

    activity = WoodcuttingActivity(test_player, test_ui, command)
    result_check = activity.check()
    assert not result_check.success


def test_low_level_requirement(test_player, test_ui) -> None:
    test_player.set_level(SkillType.WOODCUTTING, 1)

    raw_in: str = 'chop birch log'
    command: Command = Command(raw_in)

    axe: ItemInstance = ITEM_PARSER.get_instance('poor copper axe')
    test_player.give(axe)
    test_player.equip_tool(axe)

    activity = WoodcuttingActivity(test_player, test_ui, command)
    result_check = activity.check()
    assert not result_check.success


def test_log_not_in_area(test_player, test_ui) -> None:
    test_player.set_level(SkillType.WOODCUTTING, 99)
    test_player.set_area('eastveil')

    raw_in: str = 'chop pine log'
    command: Command = Command(raw_in)

    axe: ItemInstance = ITEM_PARSER.get_instance('poor copper axe')
    test_player.give(axe)
    test_player.equip_tool(axe)

    activity = WoodcuttingActivity(test_player, test_ui, command)
    result_check = activity.check()
    assert not result_check.success


def test_check_passes_with_all_requirements(test_player, test_ui) -> None:
    test_player.set_level(SkillType.WOODCUTTING, 99)

    raw_in: str = 'chop pine log'
    command: Command = Command(raw_in)

    axe: ItemInstance = ITEM_PARSER.get_instance('poor copper axe')
    test_player.give(axe)
    test_player.equip_tool(axe)

    activity = WoodcuttingActivity(test_player, test_ui, command)
    result_check = activity.check()
    assert result_check.success
