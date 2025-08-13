from Pydle.util.Result import Result
from Pydle.util.items.ItemInstance import ItemInstance
from Pydle.util.items.ItemParser import ITEM_PARSER
from Pydle.util.player.SkillType import SkillType
from Pydle.util.player.EquipmentSlot import EquipmentSlot
from Pydle.util.player.ToolSlot import ToolSlot
from Pydle.util.player.Player import Player, PlayerSaveData


def test_add_xp_and_level(test_player):
    base_level: int = test_player.get_level(SkillType.FISHING)
    test_player.add_xp(SkillType.FISHING, 5000.)

    assert test_player.get_level(SkillType.FISHING) > base_level


def test_set_xp_and_level(test_player):
    test_player.set_xp(SkillType.FISHING, 200.)
    assert test_player.get_skill(SkillType.FISHING).xp == 200.

    test_player.set_level(SkillType.FISHING, 5.)
    assert test_player.get_level(SkillType.FISHING) == 5.


def test_hitpoints_damage_and_healing(test_player):
    max_hp: int = test_player.get_max_hitpoints()
    assert test_player.hitpoints == max_hp

    test_player.damage(10)
    assert test_player.hitpoints == max_hp - 10

    test_player.heal(5)
    assert test_player.hitpoints == max_hp - 5

    test_player.heal_full()
    assert test_player.hitpoints == max_hp


def test_give_remove_and_has(test_player):
    item_instance: ItemInstance = ITEM_PARSER.get_instance('poor copper pickaxe')
    assert not test_player.has(item_instance)

    test_player.give(item_instance)
    assert test_player.has(item_instance)

    test_player.remove(item_instance)
    assert not test_player.has(item_instance)


def test_tool_equipping_flow(test_player):
    item_instance: ItemInstance = ITEM_PARSER.get_instance('poor copper pickaxe')
    test_player.give(item_instance)
    result: Result = test_player.equip_tool(item_instance)

    assert result.success
    assert test_player.get_tool(ToolSlot.PICKAXE) == item_instance

    result = test_player.unequip_tool(item_instance)

    assert result.success
    assert test_player.get_tool(ToolSlot.PICKAXE) is None


def test_equipment_equipping_flow(test_player):
    item_instance: ItemInstance = ITEM_PARSER.get_instance('poor copper longsword')
    test_player.give(item_instance)
    result: Result = test_player.equip(item_instance)

    assert result.success
    assert test_player.get_equipment(EquipmentSlot.WEAPON) == item_instance

    result = test_player.unequip(item_instance)

    assert result.success
    assert test_player.get_equipment(EquipmentSlot.WEAPON) is None


def test_equip_tool_fails_without_item(test_player):
    item_instance: ItemInstance = ITEM_PARSER.get_instance('poor copper pickaxe')
    result = test_player.equip_tool(item_instance)

    assert not result.success
    assert test_player.get_tool(ToolSlot.PICKAXE) is None


def test_equip_equipment_fails_without_item(test_player):
    item_instance: ItemInstance = ITEM_PARSER.get_instance('poor copper longsword')
    result = test_player.equip(item_instance)

    assert not result.success
    assert test_player.get_equipment(EquipmentSlot.WEAPON) is None


def test_unequip_tool_fails_wrong_item(test_player):
    first_item_instance: ItemInstance = ITEM_PARSER.get_instance('poor copper pickaxe')
    second_item_instance: ItemInstance = ITEM_PARSER.get_instance('poor iron pickaxe')

    test_player.give(first_item_instance)
    test_player.equip_tool(first_item_instance)

    result = test_player.unequip_tool(second_item_instance)
    assert not result.success

    assert test_player.get_tool(ToolSlot.PICKAXE) == first_item_instance
    assert not test_player.has(second_item_instance)
    assert not test_player.has(first_item_instance)


def test_unequip_equipment_fails_wrong_item(test_player):
    first_item_instance: ItemInstance = ITEM_PARSER.get_instance('poor copper longsword')
    second_item_instance: ItemInstance = ITEM_PARSER.get_instance('poor iron longsword')

    test_player.give(first_item_instance)
    test_player.equip(first_item_instance)

    result = test_player.unequip(second_item_instance)
    assert not result.success

    assert test_player.get_equipment(EquipmentSlot.WEAPON) == first_item_instance
    assert not test_player.has(second_item_instance)
    assert not test_player.has(first_item_instance)


def test_stats_reflect_equipment(test_player):
    base_stats = test_player.stats.copy()

    item_instance: ItemInstance = ITEM_PARSER.get_instance('poor copper longsword')
    test_player.give(item_instance)
    test_player.equip(item_instance)

    assert test_player.stats != base_stats


def test_save_and_load(tmp_path):
    save_file = tmp_path / 'player.json'
    player: Player = Player(save_file=str(save_file), name='Tester')

    item_instance: ItemInstance = ITEM_PARSER.get_instance('poor copper pickaxe')
    player.give(item_instance)
    player.equip_tool(item_instance)

    player.save()
    assert save_file.is_file()

    loaded: Player = Player(save_file=str(save_file))
    assert loaded.name == 'Tester'
    assert loaded.get_tool(ToolSlot.PICKAXE) is not None


def test_player_save_data_roundtrip(test_player):
    item_instance = ITEM_PARSER.get_instance('poor copper pickaxe')
    test_player.give(item_instance)
    test_player.equip_tool(item_instance)

    save_data = PlayerSaveData(
        name=test_player.name,
        area=test_player.area,
        items=test_player.bank.to_dict(),
        skills=test_player.skills.to_dict(),
        tools=test_player.tools.to_dict(),
        equipment=test_player.equipment.to_dict(),
        updated_effects=test_player.updated_effects.to_dict(),
    )

    save_dict = save_data.to_dict()
    restored = PlayerSaveData.from_dict(save_dict)

    assert restored.name == test_player.name
    assert restored.area == test_player.area
    assert restored.skills == test_player.skills.to_dict()
    assert restored.tools == test_player.tools.to_dict()
    assert restored.equipment == test_player.equipment.to_dict()
