from OSRSsim.util.structures.Bank import Bank


def test_instantiate():
    bank = Bank({'a': 1, 'b': 2, 'c': 0, 'd': -1})

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

    assert bank == Bank({
        'a': 4, 'b': 2, 'c': 5
    })

    bank.add({'a': 0, 'b': 2, 'd': 1})
    assert bank == Bank({
        'a': 4, 'b': 4, 'c': 5, 'd': 1
    })

    new_bank = Bank({'a': 0, 'c': 3, 'e': 1})
    bank.add(new_bank)
    assert bank == Bank({
        'a': 4, 'b': 4, 'c': 8, 'd': 1, 'e': 1
    })


def test_remove():
    bank = Bank({'a': 1, 'b': 2, 'c': 3, 'd': 4})

    bank.remove('a', 1)
    bank.remove('b', 1)

    bank.remove({'c': 1, 'd': 2})

    try:
        bank.remove('e', 1)
    except KeyError:
        pass

    assert not bank.contains('a')
    assert bank.quantity('b') == 1
    assert bank.quantity('c') == 2
    assert bank.quantity('d') == 2
    assert not bank.contains('e')


def test_contains():
    bank = Bank({'a': 1, 'b': 2})

    assert bank.contains('a')
    assert not bank.contains('c')

    assert bank.contains('a', 1)
    assert bank.contains('b', 2)
    assert bank.contains('b', 0)
    assert not bank.contains('b', 3)
    assert not bank.contains('c', 0)
    assert not bank.contains('c', 2)

    assert bank.contains({'a': 1, 'b': 1})
    assert not bank.contains({'a': 1, 'b': 1, 'c': 2})
    assert not bank.contains({'a': 3, 'b': 1})


def test_quantity():
    bank = Bank({'a': 1, 'b': 2})

    assert bank.quantity('a') == 1
    assert bank.quantity('b') == 2
    assert bank.quantity('c') == 0


def test_equality():
    bank1 = Bank({'a': 1, 'b': 2})
    bank2 = Bank({'a': 1, 'b': 2})

    assert bank1 == bank2

    bank = Bank({'a': 1})
    assert not bank1 == bank

    bank = Bank({'a': 1, 'b': 2, 'c': 1})
    assert not bank1 == bank

    bank = Bank({'a': 2, 'b': 2})
    assert not bank1 == bank

    bank = Bank()
    assert not bank1 == bank

    assert bank == Bank()
