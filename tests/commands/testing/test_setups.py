from Pydle.commands.testing.setups import SetupManager
from Pydle.util.items.ItemParser import ITEM_PARSER


def test_names_and_has_setup():
    manager = SetupManager()

    assert 'skilling' in manager.names()
    assert manager.has_setup('skilling')
    assert not manager.has_setup('unknown')


def test_apply_skilling_setup_gives_expected_items(test_player):
    manager = SetupManager()
    pickaxe = ITEM_PARSER.get_instance('poor copper pickaxe')

    assert not test_player.has(pickaxe)

    manager.apply(test_player, 'skilling')

    assert test_player.has(pickaxe)
