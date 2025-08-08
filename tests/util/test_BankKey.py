from Pydle.util.items.ItemParser import ITEM_PARSER
from Pydle.util.player.Bank import BankKey
from Pydle.util.items.Quality import Quality


def test_equal():
    bank_key1 = BankKey(ITEM_PARSER.get_id_by_name('copper ore'))
    bank_key2 = BankKey(ITEM_PARSER.get_id_by_name('copper ore'))
    bank_key3 = BankKey(ITEM_PARSER.get_id_by_name('silver ore'))
    bank_key4 = BankKey(ITEM_PARSER.get_id_by_name('silver ore'), Quality.GOOD)

    assert bank_key1 == bank_key2
    assert bank_key1 != bank_key3
    assert bank_key3 != bank_key4
