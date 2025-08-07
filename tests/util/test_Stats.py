from Pydle.util.player.Stats import Stats


def test_stats_add():
    stats_1 = Stats({
        'accuracy': 2,
        'physical_strength': 6,
        'physical_defense': 3,
        'magical_barrier': -3,
    })

    stats_2 = Stats({
        'accuracy': 2,
        'physical_strength': 6,
        'evasiveness': 1,
        'magical_barrier': -3,
    })

    stats_sum = stats_1 + stats_2

    assert stats_sum['physical_strength'] == 12
    assert stats_sum['physical_defense'] == 3
    assert stats_sum['magical_barrier'] == -6
    assert stats_sum['accuracy'] == 4
    assert stats_sum['evasiveness'] == 1
