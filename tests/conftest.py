# conftest.py
import pytest

from Pydle.lib.item_sets import NEW_PLAYER_ITEMS
from Pydle.util.items.ItemParser import ITEM_PARSER
from Pydle.util.player.Bank import Bank
from Pydle.util.player.Player import Player
from Pydle.util.structures.UserInterface import NullUserInterface


@pytest.fixture
def sample_bank():
    bank = (
        Bank()
        .add(ITEM_PARSER.get_instance('copper ore', 1))
        .add(ITEM_PARSER.get_instance('silver ore', 2))
        .add(ITEM_PARSER.get_instance('iron ore', 3))
        .add(ITEM_PARSER.get_instance('coal', 4))
    )
    return bank


@pytest.fixture
def test_player():
    player: Player = Player(name='TestPlayer')
    player.remove(NEW_PLAYER_ITEMS)
    return player


@pytest.fixture
def test_ui():
    return NullUserInterface()
