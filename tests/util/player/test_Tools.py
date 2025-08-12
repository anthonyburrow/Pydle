import pytest

from Pydle.util.Result import Result
from Pydle.util.items.ItemInstance import ItemInstance
from Pydle.util.items.ItemParser import ITEM_PARSER
from Pydle.util.player.ToolSlot import ToolSlot


def test_equip_success(test_player):
    item_instance: ItemInstance = ITEM_PARSER.get_instance('poor copper pickaxe')

    test_player.give(item_instance)
    assert test_player.has(item_instance)

    result: Result = test_player.equip_tool(item_instance)

    assert result.success
    assert test_player.get_tool(ToolSlot.PICKAXE) == item_instance
    assert not test_player.has(item_instance)


def test_equip_fail_no_item(test_player):
    item_instance: ItemInstance = ITEM_PARSER.get_instance('poor copper pickaxe')

    result: Result = test_player.equip_tool(item_instance)

    assert not result.success
    assert test_player.get_tool(ToolSlot.PICKAXE) is None


def test_equip_replaces_existing(test_player):
    first_item: ItemInstance = ITEM_PARSER.get_instance('poor copper pickaxe')
    second_item: ItemInstance = ITEM_PARSER.get_instance('poor iron pickaxe')

    test_player.give(first_item)
    test_player.equip_tool(first_item)

    test_player.give(second_item)
    result: Result = test_player.equip_tool(second_item)

    assert result.success
    assert test_player.get_tool(ToolSlot.PICKAXE) == second_item
    assert test_player.has(first_item)


def test_unequip_success(test_player):
    item_instance: ItemInstance = ITEM_PARSER.get_instance('poor copper pickaxe')

    test_player.give(item_instance)
    test_player.equip_tool(item_instance)
    assert not test_player.has(item_instance)

    result: Result = test_player.unequip_tool(item_instance)

    assert result.success
    assert test_player.get_tool(ToolSlot.PICKAXE) is None
    assert test_player.has(item_instance)


def test_unequip_fail_not_equipped(test_player):
    item_instance: ItemInstance = ITEM_PARSER.get_instance('poor copper pickaxe')

    result: Result = test_player.unequip_tool(item_instance)

    assert not result.success
    assert test_player.get_tool(ToolSlot.PICKAXE) is None


def test_unequip_fail_wrong_item(test_player):
    first_item: ItemInstance = ITEM_PARSER.get_instance('poor copper pickaxe')
    second_item: ItemInstance = ITEM_PARSER.get_instance('poor iron pickaxe')

    test_player.give(first_item)
    test_player.equip_tool(first_item)

    result: Result = test_player.unequip_tool(second_item)

    assert not result.success
    assert test_player.get_tool(ToolSlot.PICKAXE) == first_item
    assert not test_player.has(second_item)
    assert not test_player.has(first_item)


def test_to_dict_and_load_from_dict(test_player):
    item_instance: ItemInstance = ITEM_PARSER.get_instance('poor copper pickaxe')

    test_player.give(item_instance)
    test_player.equip_tool(item_instance)

    tools_dict = test_player.tools.to_dict()

    assert tools_dict['PICKAXE'] == item_instance.to_dict()
    assert set(tools_dict.keys()) == {slot.name for slot in ToolSlot}

    new_player = test_player.__class__(name='NewPlayer')
    new_player.tools.load_from_dict(tools_dict)

    assert isinstance(new_player.get_tool(ToolSlot.PICKAXE), ItemInstance)
    assert new_player.get_tool(ToolSlot.PICKAXE).name == item_instance.name


def test_setitem_invalid_key(test_player):
    with pytest.raises(KeyError):
        test_player.tools['not-a-slot'] == None
