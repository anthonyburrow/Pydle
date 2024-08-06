from Pydle.util.structures.Stats import Stats


def test_stats_add():
    stats_1 = Stats({
        'attack_melee': 2,
        'strength_melee': 6,
        'defense_melee': 3,
        'defense_magic': -3,
    })

    stats_2 = Stats({
        'attack_melee': 2,
        'strength_melee': 6,
        'defense_ranged': 1,
        'defense_magic': -3,
    })

    stats_sum = stats_1 + stats_2

    assert stats_sum['attack_melee'] == 4
    assert stats_sum['strength_melee'] == 12
    assert stats_sum['defense_melee'] == 3
    assert stats_sum['defense_ranged'] == 1
    assert stats_sum['defense_magic'] == -6
    assert stats_sum['attack_ranged'] == 0
