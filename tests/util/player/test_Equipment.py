import pytest

from Pydle.util.Result import Result
from Pydle.util.items.ItemInstance import ItemInstance
from Pydle.util.items.ItemParser import ITEM_PARSER
from Pydle.util.player.EquipmentSlot import EquipmentSlot


def test_equip_success(test_player):
    item_instance: ItemInstance = ITEM_PARSER.get_instance('poor copper longsword')
    test_player.give(item_instance)
    assert test_player.has(item_instance)

    result: Result = test_player.equip(item_instance)

    assert result.success
    assert test_player.get_equipment(EquipmentSlot.WEAPON) == item_instance
    assert not test_player.has(item_instance)


def test_equip_fail_no_item(test_player):
    item_instance: ItemInstance = ITEM_PARSER.get_instance('poor copper longsword')
    result: Result = test_player.equip(item_instance)

    assert not result.success
    assert test_player.get_equipment(EquipmentSlot.WEAPON) is None


def test_equip_replaces_existing(test_player):
    first_item: ItemInstance = ITEM_PARSER.get_instance('poor copper longsword')
    second_item: ItemInstance = ITEM_PARSER.get_instance('poor iron longsword')

    test_player.give(first_item)
    test_player.equip(first_item)

    test_player.give(second_item)
    result: Result = test_player.equip(second_item)

    assert result.success
    assert test_player.get_equipment(EquipmentSlot.WEAPON) == second_item
    assert test_player.has(first_item)


def test_unequip_success(test_player):
    item_instance: ItemInstance = ITEM_PARSER.get_instance('poor copper longsword')

    test_player.give(item_instance)
    test_player.equip(item_instance)
    assert not test_player.has(item_instance)

    result: Result = test_player.unequip(item_instance)

    assert result.success
    assert test_player.get_equipment(EquipmentSlot.WEAPON) is None
    assert test_player.has(item_instance)


def test_unequip_fail_not_equipped(test_player):
    item_instance: ItemInstance = ITEM_PARSER.get_instance('poor copper longsword')
    result: Result = test_player.unequip(item_instance)

    assert not result.success
    assert test_player.get_equipment(EquipmentSlot.WEAPON) is None


def test_unequip_fail_wrong_item(test_player):
    first_item: ItemInstance = ITEM_PARSER.get_instance('poor copper longsword')
    second_item: ItemInstance = ITEM_PARSER.get_instance('poor iron longsword')

    test_player.give(first_item)
    test_player.equip(first_item)

    result: Result = test_player.unequip(second_item)

    assert not result.success
    assert test_player.get_equipment(EquipmentSlot.WEAPON) == first_item
    assert not test_player.has(second_item)
    assert not test_player.has(first_item)


def test_to_dict_and_load_from_dict(test_player):
    item_instance: ItemInstance = ITEM_PARSER.get_instance('poor copper longsword')
    test_player.give(item_instance)
    test_player.equip(item_instance)

    eq_dict = test_player.equipment.to_dict()
    assert eq_dict['WEAPON'] == item_instance.to_dict()
    assert set(eq_dict.keys()) == {slot.name for slot in EquipmentSlot}

    new_player = test_player.__class__(name='NewPlayer')
    new_player.equipment.load_from_dict(eq_dict)

    loaded_item = new_player.get_equipment(EquipmentSlot.WEAPON)
    assert isinstance(loaded_item, ItemInstance)
    assert loaded_item.name == item_instance.name


def test_stats_update_on_equip_and_unequip(test_player):
    item_instance: ItemInstance = ITEM_PARSER.get_instance('poor copper longsword')
    base_stats: dict = test_player.equipment.stats.copy()

    test_player.give(item_instance)
    test_player.equip(item_instance)
    assert test_player.equipment.stats != base_stats

    test_player.unequip(item_instance)
    assert test_player.equipment.stats == base_stats


def test_setitem_invalid_key(test_player):
    with pytest.raises(KeyError):
        test_player.equipment['not-a-slot'] = None
