import numpy as np

from OSRSsim.util.structures import LootTable


def test_null_roll():
    table = LootTable()

    table.roll()


def test_weighted():
    table = LootTable()

    table.add('a', 1, 1.)
    table.add('b', 2)
    table.add('c', weight=2.)

    try:
        table.add('a')
    except KeyError:
        pass

    probabilities = np.array([0.25, 0.25, 0.5])
    assert np.array_equal(probabilities, table._weighted_probabilities)


def test_sampling():
    print()

    table = LootTable()

    table.add('A', 1, 6.)
    table.add('B', 2, 3.)
    table.add('C', 1, 1.)

    table.tertiary('D', 1. / 10.)
    table.tertiary('E', 1. / 300.)

    table.every('F')
    table.every('G', 3)

    N = 1000
    loot = table.roll(N)

    print(f'TEST SAMPLING: N = {N}')
    print(f'  EXPECTED:')
    print(f'  [W] A (6/10) ~ {int(N * 6. / 10.)}')
    print(f'    RECEIVED {loot.quantity("A")}')
    print(f'  [W] B 2x (3/10) ~ {2 * int(N * 3. / 10.)}')
    print(f'    RECEIVED {loot.quantity("B")}')
    print(f'  [W] C (1/10) ~ {int(N * 1. / 10.)}')
    print(f'    RECEIVED {loot.quantity("C")}')
    print(f'  [T] D (1/10) ~ {N / 10.:.3f}')
    print(f'    RECEIVED {loot.quantity("D")}')
    print(f'  [T] E (1/300) ~ {N / 300.:.3f}')
    print(f'    RECEIVED {loot.quantity("E")}')
    print(f'  [E] F = {N}')
    print(f'    RECEIVED {loot.quantity("F")}')
    print(f'  [E] G = {N * 3}')
    print(f'    RECEIVED {loot.quantity("G")}')

    assert loot.quantity('A') + int(loot.quantity('B') / 2.) + loot.quantity('C') == N
    assert loot.quantity('B') % 2 == 0
    assert loot.quantity('F') == N
    assert loot.quantity('G') == N * 3
