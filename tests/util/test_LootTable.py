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
    print()

    table = LootTable()

    table.add('copper ore', 1, 6.)
    table.add('iron ore', 2, 3.)
    table.add('coal', 1, 1.)

    table.tertiary('mithril ore', 1. / 10.)
    table.tertiary('adamantite ore', 1. / 300.)

    table.every('runite ore')
    table.every('orikalkum ore', 3)

    N = 1000
    loot = table.roll(N)

    print(f'TEST SAMPLING: N = {N}')
    print(f'  EXPECTED:')
    print(f'  [W] Copper (6/10) ~ {int(N * 6. / 10.)}')
    print(f'    RECEIVED {loot.quantity('copper ore')}')
    print(f'  [W] Iron 2x (3/10) ~ {2 * int(N * 3. / 10.)}')
    print(f'    RECEIVED {loot.quantity('iron ore')}')
    print(f'  [W] Coal (1/10) ~ {int(N * 1. / 10.)}')
    print(f'    RECEIVED {loot.quantity('coal')}')
    print(f'  [T] Mithril (1/10) ~ {N / 10.:.3f}')
    print(f'    RECEIVED {loot.quantity('mithril ore')}')
    print(f'  [T] Adamantite (1/300) ~ {N / 300.:.3f}')
    print(f'    RECEIVED {loot.quantity('adamantite ore')}')
    print(f'  [E] Runite = {N}')
    print(f'    RECEIVED {loot.quantity('runite ore')}')
    print(f'  [E] Orikalkum = {N * 3}')
    print(f'    RECEIVED {loot.quantity('orikalkum ore')}')

    assert loot.quantity('copper ore') + int(loot.quantity('iron ore') / 2.) + loot.quantity('coal') == N
    assert loot.quantity('iron ore') % 2 == 0
    assert loot.quantity('runite ore') == N
    assert loot.quantity('orikalkum ore') == N * 3
