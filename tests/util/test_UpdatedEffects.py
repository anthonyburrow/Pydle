from OSRSsim.util.structures.UpdatedEffects import UpdatedEffects


def test_update():
    effects = UpdatedEffects()

    effects.add_effect('test1', 2)
    effects.add_effect('test2', 1)

    assert 'test1' in effects
    assert 'test2' in effects

    effects.update_effects()
    assert 'test1' in effects
    assert 'test2' not in effects

    effects.update_effects()
    assert 'test1' not in effects
    assert len(effects) == 0


def test_overwrite_effect():
    effects = UpdatedEffects()

    effects.add_effect('test1', 2)
    effects.add_effect('test2', 1)

    effects.update_effects()
    effects.add_effect('test1', 2)
    assert effects['test1'] == 2
