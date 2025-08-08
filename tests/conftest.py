# conftest.py
import pytest

from Pydle.util.items.ItemParser import ITEM_PARSER
from Pydle.util.player.Bank import Bank


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
