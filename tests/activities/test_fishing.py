from Pydle.commands.Command import Command
from Pydle.commands.Activity import ActivityCheckResult
from Pydle.commands.activities.skilling.fishing import FishingActivity
from Pydle.util.items.ItemInstance import ItemInstance
from Pydle.util.items.ItemParser import ITEM_PARSER
from Pydle.util.player.SkillType import SkillType


def test_missing_fishing_rod(test_player, test_ui) -> None:
    test_player.set_level(SkillType.FISHING, 99)

    raw_in: str = 'fish raw shrimp'
    command: Command = Command(raw_in)

    activity: FishingActivity = FishingActivity(test_player, test_ui, command)
    result_check: ActivityCheckResult = activity.check()
    assert not result_check.success

    rod: ItemInstance = ITEM_PARSER.get_instance('poor copper fishing rod')
    test_player.give(rod)
    test_player.equip_tool(rod)

    activity = FishingActivity(test_player, test_ui, command)
    result_check = activity.check()
    assert result_check.success


def test_misspelled_fish(test_player, test_ui) -> None:
    test_player.set_level(SkillType.FISHING, 99)

    raw_in: str = 'fish raw shrmp'
    command: Command = Command(raw_in)

    rod: ItemInstance = ITEM_PARSER.get_instance('poor copper fishing rod')
    test_player.give(rod)
    test_player.equip_tool(rod)

    activity = FishingActivity(test_player, test_ui, command)
    result_check = activity.check()
    assert not result_check.success


def test_low_level_requirement(test_player, test_ui) -> None:
    test_player.set_level(SkillType.FISHING, 1)

    raw_in: str = 'fish raw anchovy'
    command: Command = Command(raw_in)

    rod: ItemInstance = ITEM_PARSER.get_instance('poor copper fishing rod')
    test_player.give(rod)
    test_player.equip_tool(rod)

    activity = FishingActivity(test_player, test_ui, command)
    result_check = activity.check()
    assert not result_check.success


def test_fish_not_in_area(test_player, test_ui) -> None:
    test_player.set_level(SkillType.FISHING, 99)
    test_player.set_area('eastveil')

    raw_in: str = 'fish raw shrimp'
    command: Command = Command(raw_in)

    rod: ItemInstance = ITEM_PARSER.get_instance('poor copper fishing rod')
    test_player.give(rod)
    test_player.equip_tool(rod)

    activity = FishingActivity(test_player, test_ui, command)
    result_check = activity.check()
    assert not result_check.success


def test_check_passes_with_all_requirements(test_player, test_ui) -> None:
    test_player.set_level(SkillType.FISHING, 99)

    raw_in: str = 'fish raw shrimp'
    command: Command = Command(raw_in)

    rod: ItemInstance = ITEM_PARSER.get_instance('poor copper fishing rod')
    test_player.give(rod)
    test_player.equip_tool(rod)

    activity = FishingActivity(test_player, test_ui, command)
    result_check = activity.check()
    assert result_check.success
