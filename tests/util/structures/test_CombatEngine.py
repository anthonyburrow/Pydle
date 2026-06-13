from Pydle.util.items.ItemParser import ITEM_PARSER
from Pydle.util.monsters.MonsterInstance import MonsterInstance
from Pydle.util.structures.CombatEngine import CombatEngine, CombatResult


def test_tick_handles_missing_weapon_slot(test_player):
    monster = MonsterInstance('goblin')
    engine = CombatEngine(test_player, monster)

    # Tick 1 always allows a monster attack timing window.
    result = engine.tick(1)

    assert isinstance(result, CombatResult)


def test_tick_handles_equipped_weapon(test_player):
    weapon = ITEM_PARSER.get_instance('poor copper longsword')
    test_player.give(weapon)
    equip_result = test_player.equip(weapon)
    assert equip_result.success

    monster = MonsterInstance('goblin')
    engine = CombatEngine(test_player, monster)

    result = engine.tick(weapon.attack_speed)

    assert isinstance(result, CombatResult)
