from Pydle.util.items.ItemParser import ITEM_PARSER
from Pydle.util.monsters.MonsterInstance import MonsterInstance
from Pydle.util.player.Player import Player
from Pydle.util.structures.Area import Area
from Pydle.util.ticks import Ticks


def test_travel_ticks_uses_distance_and_tick_size():
    area = Area(name='Farlands', coordinates=(3, 4))

    expected_ticks = int(60.0 * 5.0 / Ticks()) + 1

    assert area.travel_ticks((0, 0)) == expected_ticks


def test_contains_helpers_match_names():
    area = Area(
        name='TestArea',
        coordinates=(0, 0),
        monsters={'goblin'},
        collectables={'parsley leaves': 1},
        fish={'raw shrimp'},
        logs={'pine log'},
        ores={'copper ore'},
    )

    monster = MonsterInstance('goblin')
    collectable = ITEM_PARSER.get_instance('parsley leaves')
    fish = ITEM_PARSER.get_instance('raw shrimp')
    log = ITEM_PARSER.get_instance('pine log')
    ore = ITEM_PARSER.get_instance('copper ore')

    assert area.contains_monster(monster)
    assert area.contains_collectable(collectable)
    assert area.contains_fish(fish)
    assert area.contains_log(log)
    assert area.contains_ore(ore)


def test_requirements_callable_signature_accepts_player():
    observed = {'player_name': ''}

    def req(player: Player) -> bool:
        observed['player_name'] = player.name
        return True

    area = Area(
        name='ReqArea',
        coordinates=(0, 0),
        requirements=[req],
    )

    test_player = Player(name='ReqTester')

    assert area.requirements[0](test_player)
    assert observed['player_name'] == 'ReqTester'
