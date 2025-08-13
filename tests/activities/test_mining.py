from Pydle.commands.Command import Command
from Pydle.commands.Activity import ActivityCheckResult
from Pydle.commands.activities.skilling.mining import MiningActivity
from Pydle.util.items.ItemInstance import ItemInstance
from Pydle.util.items.ItemParser import ITEM_PARSER
from Pydle.util.player.SkillType import SkillType


def test_missing_pickaxe(test_player, test_ui):
    test_player.set_level(SkillType.MINING, 99)

    raw_in: str = 'mine copper ore'
    command: Command = Command(raw_in)

    activity: MiningActivity = MiningActivity(test_player, test_ui, command)
    result_check: ActivityCheckResult = activity.check()
    assert not result_check.success

    pickaxe: ItemInstance = ITEM_PARSER.get_instance('poor copper pickaxe')
    test_player.give(pickaxe)
    test_player.equip_tool(pickaxe)

    activity: MiningActivity = MiningActivity(test_player, test_ui, command)
    result_check: ActivityCheckResult = activity.check()
    assert result_check.success


def test_misspelled_ore(test_player, test_ui):
    test_player.set_level(SkillType.MINING, 99)

    raw_in: str = 'mine irn ore'
    command: Command = Command(raw_in)

    pickaxe: ItemInstance = ITEM_PARSER.get_instance('poor copper pickaxe')
    test_player.give(pickaxe)
    test_player.equip_tool(pickaxe)

    activity: MiningActivity = MiningActivity(test_player, test_ui, command)
    result_check: ActivityCheckResult = activity.check()
    assert not result_check.success


def test_low_level_requirement(test_player, test_ui):
    test_player.set_level(SkillType.MINING, 1)

    raw_in: str = 'mine iron ore'
    command: Command = Command(raw_in)

    pickaxe: ItemInstance = ITEM_PARSER.get_instance('poor copper pickaxe')
    test_player.give(pickaxe)
    test_player.equip_tool(pickaxe)

    activity: MiningActivity = MiningActivity(test_player, test_ui, command)
    result_check: ActivityCheckResult = activity.check()
    assert not result_check.success


def test_ore_not_in_area(test_player, test_ui):
    test_player.set_level(SkillType.MINING, 99)
    test_player.set_area('eastveil')

    raw_in: str = 'mine copper ore'
    command: Command = Command(raw_in)

    pickaxe: ItemInstance = ITEM_PARSER.get_instance('poor copper pickaxe')
    test_player.give(pickaxe)
    test_player.equip_tool(pickaxe)

    activity: MiningActivity = MiningActivity(test_player, test_ui, command)
    result_check: ActivityCheckResult = activity.check()
    assert not result_check.success


def test_check_passes_with_all_requirements(test_player, test_ui):
    test_player.set_level(SkillType.MINING, 99)

    raw_in: str = 'mine copper ore'
    command: Command = Command(raw_in)

    pickaxe: ItemInstance = ITEM_PARSER.get_instance('poor copper pickaxe')
    test_player.give(pickaxe)
    test_player.equip_tool(pickaxe)

    activity: MiningActivity = MiningActivity(test_player, test_ui, command)
    result_check: ActivityCheckResult = activity.check()
    assert result_check.success
