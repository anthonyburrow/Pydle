from Pydle.util.structures.Bank import Bank


def test_instantiate():
    bank = Bank({'copper ore': 1, 'iron ore': 2, 'coal': 0, 'gold ore': -1})

    assert bank.contains('copper ore')
    assert not bank.contains('coal')
    assert not bank.contains('gold ore')


def test_add():
    bank = Bank({'copper ore': 1, 'iron ore': 2})

    try:
        bank.add('copper ore', -1)
    except ValueError:
        pass

    bank.add('copper ore', 2)
    bank.add('copper ore')
    bank.add('coal', 5)

    assert bank == Bank({
        'copper ore': 4, 'iron ore': 2, 'coal': 5
    })

    bank.add({'copper ore': 0, 'iron ore': 2, 'gold ore': 1})
    assert bank == Bank({
        'copper ore': 4, 'iron ore': 4, 'coal': 5, 'gold ore': 1
    })

    new_bank = Bank({'copper ore': 0, 'coal': 3, 'adamantite ore': 1})
    bank.add(new_bank)
    assert bank == Bank({
        'copper ore': 4, 'iron ore': 4, 'coal': 8, 'gold ore': 1, 'adamantite ore': 1
    })


def test_remove():
    bank = Bank({'copper ore': 1, 'iron ore': 2, 'coal': 3, 'gold ore': 4})

    bank.remove('copper ore', 1)
    bank.remove('iron ore', 1)

    bank.remove({'coal': 1, 'gold ore': 2})

    try:
        bank.remove('adamantite ore', 1)
    except KeyError:
        pass

    assert not bank.contains('copper ore')
    assert bank.quantity('iron ore') == 1
    assert bank.quantity('coal') == 2
    assert bank.quantity('gold ore') == 2
    assert not bank.contains('adamantite ore')


def test_contains():
    bank = Bank({'copper ore': 1, 'iron ore': 2})

    assert bank.contains('copper ore')
    assert not bank.contains('coal')

    assert bank.contains('copper ore', 1)
    assert bank.contains('iron ore', 2)
    assert bank.contains('iron ore', 0)
    assert not bank.contains('iron ore', 3)
    assert not bank.contains('coal', 0)
    assert not bank.contains('coal', 2)

    assert bank.contains({'copper ore': 1, 'iron ore': 1})
    assert not bank.contains({'copper ore': 1, 'iron ore': 1, 'coal': 2})
    assert not bank.contains({'copper ore': 3, 'iron ore': 1})


def test_quantity():
    bank = Bank({'copper ore': 1, 'iron ore': 2})

    assert bank.quantity('copper ore') == 1
    assert bank.quantity('iron ore') == 2
    assert bank.quantity('coal') == 0


def test_equality():
    bank1 = Bank({'copper ore': 1, 'iron ore': 2})
    bank2 = Bank({'copper ore': 1, 'iron ore': 2})

    assert bank1 == bank2

    bank = Bank({'copper ore': 1})
    assert not bank1 == bank

    bank = Bank({'copper ore': 1, 'iron ore': 2, 'coal': 1})
    assert not bank1 == bank

    bank = Bank({'copper ore': 2, 'iron ore': 2})
    assert not bank1 == bank

    bank = Bank()
    assert not bank1 == bank

    assert bank == Bank()


def test_empty():
    bank = Bank()
    assert not bank

    bank.add({'copper ore': 1})
    assert bank
