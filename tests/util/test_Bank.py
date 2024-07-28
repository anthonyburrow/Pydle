from OSRSsim.util.structures.Bank import Bank


def test_instantiate():
    bank = Bank({'a': 1, 'b': 2, 'c': 0, 'd': -1})

    # Removal of zero/negative quantities
    assert bank.contains('a')
    assert not bank.contains('c')
    assert not bank.contains('d')


def test_add():
    bank = Bank({'a': 1, 'b': 2})

    try:
        bank.add('a', -1)
    except ValueError:
        pass

    bank.add('a', 2)
    bank.add('a')
    bank.add('c', 5)

    # Can maybe make these checks into Bank __eq__ checks
    assert bank.quantity('a') == 4
    assert bank.quantity('b') == 2
    assert bank.quantity('c') == 5

    bank.add({'a': 0, 'b': 2, 'd': 1})

    assert bank.quantity('a') == 4
    assert bank.quantity('b') == 4
    assert bank.quantity('d') == 1

    new_bank = Bank({'a': 0, 'c': 3, 'e': 1})
    bank.add(new_bank)

    assert bank.quantity('a') == 4
    assert bank.quantity('c') == 8
    assert bank.quantity('e') == 1


def test_remove():
    bank = Bank({'a': 1, 'b': 2})

    bank.remove('a', 1)
    bank.remove('b', 1)

    try:
        bank.remove('c', 1)
    except ValueError:
        pass

    assert not bank.contains('a')
    assert bank.quantity('b') == 1
    assert not bank.contains('c')


def test_contains():
    bank = Bank({'a': 1, 'b': 2})

    assert bank.contains('a')
    assert not bank.contains('c')

    assert bank.contains('a', 1)
    assert bank.contains('b', 2)
    assert bank.contains('b', 0)
    assert not bank.contains('c', 0)
    assert not bank.contains('c', 2)


def test_quantity():
    bank = Bank({'a': 1, 'b': 2})

    assert bank.quantity('a') == 1
    assert bank.quantity('b') == 2
    assert bank.quantity('c') == 0
