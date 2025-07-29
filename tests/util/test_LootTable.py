import numpy as np

from Pydle.util.structures.LootTable import LootTable


def test_null_roll():
    table = LootTable()

    table.roll()


def test_weighted():
    table = LootTable()

    table.add('copper ore', 1, 1.)
    table.add('iron ore', 2)
    table.add('coal', weight=2.)

    try:
        table.add('copper ore')
    except KeyError:
        pass

    probabilities = np.array([0.25, 0.25, 0.5])
    assert np.array_equal(probabilities, table._weighted_probabilities)


def test_sampling():
    table = LootTable()

    table.add('copper ore', 1, 6.)
    table.add('iron ore', 2, 3.)
    table.add('coal', 1, 1.)

    table.tertiary('gold ore', 1. / 10.)
    table.tertiary('adamantite ore', 1. / 300.)

    table.every('black ore')
    table.every('wyrmheart ore', 3)

    N = 10000
    loot = table.roll(N)

    def is_likely(value: int, p: float):
        std = int(np.sqrt(N * p * (1. - p))) + 1
        mean = int(N * p)
        return mean - 5 * std < value < mean + 5 * std

    assert is_likely(loot.quantity('copper ore'), 0.6)
    assert is_likely(int(loot.quantity('iron ore') * 0.5), 0.3)
    assert is_likely(loot.quantity('coal'), 0.1)
    assert is_likely(loot.quantity('gold ore'), 0.1)
    assert is_likely(loot.quantity('adamantite ore'), 1. / 300.)

    assert loot.quantity('copper ore') + int(loot.quantity('iron ore') / 2.) + loot.quantity('coal') == N
    assert loot.quantity('iron ore') % 2 == 0
    assert loot.quantity('black ore') == N
    assert loot.quantity('wyrmheart ore') == N * 3
