import numpy as np

from Pydle.util.items.ItemParser import ITEM_PARSER
from Pydle.util.player.Bank import Bank
from Pydle.util.player.BankKey import BankKey
from Pydle.util.structures.LootTable import LootTable


def is_likely(n_received: int, N: int, p: float, quantity: int = 1):
    std = int(np.sqrt(N * p * (1. - p))) + 1
    mean = int(N * p)
    return mean - 5 * std < n_received / float(quantity) < mean + 5 * std


def test_null_roll():
    table = LootTable()

    assert not table.roll()


def test_weighted():
    table = (
        LootTable()
        .add(ITEM_PARSER.get_instance('copper ore'), 1.)
        .add(ITEM_PARSER.get_instance('silver ore', 2), 1.)
        .add(ITEM_PARSER.get_instance('iron ore'), 2.)
    )

    N: int = 5000
    loot: Bank = table.roll(N)

    n_copper: int = loot.quantity(BankKey(ITEM_PARSER.get_id_by_name('copper ore')))
    n_silver: int = loot.quantity(BankKey(ITEM_PARSER.get_id_by_name('silver ore')))
    n_iron: int = loot.quantity(BankKey(ITEM_PARSER.get_id_by_name('iron ore')))

    assert is_likely(n_copper, N, 0.25)
    assert is_likely(n_silver, N, 0.25, 2)
    assert is_likely(n_iron, N, 0.5)
    assert n_copper + n_silver / 2 + n_iron == N
    assert n_silver % 2 == 0


def test_empty_weight():
    table = (
        LootTable()
        .add(ITEM_PARSER.get_instance('copper ore'), 1.)
        .add(ITEM_PARSER.get_instance('silver ore', 2), 1.)
        .add_empty(2.)
    )

    N: int = 10000
    loot: Bank = table.roll(N)

    n_copper: int = loot.quantity(BankKey(ITEM_PARSER.get_id_by_name('copper ore')))
    n_silver: int = loot.quantity(BankKey(ITEM_PARSER.get_id_by_name('silver ore')))

    assert is_likely(n_copper, N, 0.25)
    assert is_likely(n_silver, N, 0.25, 2)
    assert n_silver % 2 == 0


def test_tertiary():
    table = (
        LootTable()
        .tertiary(ITEM_PARSER.get_instance('copper ore'), 0.1)
        .tertiary(ITEM_PARSER.get_instance('silver ore', 2), 1. / 300.)
    )

    N: int = 10000
    loot: Bank = table.roll(N)

    n_copper: int = loot.quantity(BankKey(ITEM_PARSER.get_id_by_name('copper ore')))
    n_silver: int = loot.quantity(BankKey(ITEM_PARSER.get_id_by_name('silver ore')))

    assert is_likely(n_copper, N, 0.1)
    assert is_likely(n_silver, N, 1. / 300., 2)
    assert n_silver % 2 == 0


def test_every():
    table = (
        LootTable()
        .every(ITEM_PARSER.get_instance('copper ore'))
        .every(ITEM_PARSER.get_instance('silver ore', 2))
    )

    N: int = 10000
    loot: Bank = table.roll(N)

    n_copper: int = loot.quantity(BankKey(ITEM_PARSER.get_id_by_name('copper ore')))
    n_silver: int = loot.quantity(BankKey(ITEM_PARSER.get_id_by_name('silver ore')))

    assert n_copper == N
    assert n_silver == N * 2
