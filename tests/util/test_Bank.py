import pytest

from Pydle.util.items.ItemInstance import ItemInstance
from Pydle.util.items.ItemParser import ITEM_PARSER
from Pydle.util.player.Bank import Bank
from Pydle.util.player.Bank import BankKey


def test_instantiate():
    item_instance: ItemInstance = ITEM_PARSER.get_instance('copper ore')

    bank: Bank = Bank({
        'copper ore': item_instance.to_dict()
    })

    assert bank.contains(item_instance)


def test_add():
    bank: Bank = (
        Bank()
        .add(ITEM_PARSER.get_instance('copper ore'))
        .add(ITEM_PARSER.get_instance('iron ore', 2))
        .add(ITEM_PARSER.get_instance('copper ore', 2))
    )

    assert bank.quantity(BankKey(ITEM_PARSER.get_id_by_name('copper ore'))) == 3
    assert bank.quantity(BankKey(ITEM_PARSER.get_id_by_name('iron ore'))) == 2
    assert bank.quantity(BankKey(ITEM_PARSER.get_id_by_name('coal'))) == 0


def test_remove(sample_bank):
    sample_bank.remove(ITEM_PARSER.get_instance('copper ore', 1))
    sample_bank.remove(ITEM_PARSER.get_instance('silver ore', 1))
    with pytest.raises(KeyError):
        sample_bank.remove(ITEM_PARSER.get_instance('iron ore', 4))

    assert not sample_bank.contains(ITEM_PARSER.get_instance('copper ore'))
    assert sample_bank.quantity(BankKey(ITEM_PARSER.get_id_by_name('silver ore'))) == 1
    assert sample_bank.quantity(BankKey(ITEM_PARSER.get_id_by_name('iron ore'))) == 3
    assert sample_bank.quantity(BankKey(ITEM_PARSER.get_id_by_name('coal'))) == 4


def test_contains(sample_bank):
    assert sample_bank.contains(ITEM_PARSER.get_instance('copper ore'))
    assert sample_bank.contains(ITEM_PARSER.get_instance('copper ore', 1))
    assert sample_bank.contains(ITEM_PARSER.get_instance('copper ore', 2))
    assert not sample_bank.contains(ITEM_PARSER.get_instance('copper ore', 2), check_quantity=True)
    assert sample_bank.contains(ITEM_PARSER.get_instance('silver ore', 2), check_quantity=True)

    assert not sample_bank.contains(ITEM_PARSER.get_instance('adamantite ore'))

    assert sample_bank.contains(sample_bank)
    assert sample_bank.contains(sample_bank, check_quantity=True)

    bank: Bank = (
        Bank()
        .add(ITEM_PARSER.get_instance('copper ore', 1))
        .add(ITEM_PARSER.get_instance('silver ore', 2))
        .add(ITEM_PARSER.get_instance('iron ore', 3))
        .add(ITEM_PARSER.get_instance('coal', 5))
    )
    assert sample_bank.contains(bank)
    assert not sample_bank.contains(bank, check_quantity=True)


def test_quantity(sample_bank):
    assert sample_bank.quantity(BankKey(ITEM_PARSER.get_id_by_name('copper ore'))) == 1
    assert sample_bank.quantity(BankKey(ITEM_PARSER.get_id_by_name('silver ore'))) == 2
    assert sample_bank.quantity(BankKey(ITEM_PARSER.get_id_by_name('adamantite ore'))) == 0


def test_empty(sample_bank):
    bank: Bank = Bank()
    assert not bank

    assert sample_bank
