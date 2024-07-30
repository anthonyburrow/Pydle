from OSRSsim.util.structures.Skill import Skill, MAX_XP, MAX_LEVEL


big_XP = 100_000_000_000


def test_leveling():
    skill = Skill('mining', 'gathering')

    skill.add_XP(82)
    assert skill.level == 1
    skill.add_XP(1)
    assert skill.level == 2

    skill.set_XP(276)
    assert skill.level == 4
    skill.add_XP(111)
    assert skill.level == 4
    skill.add_XP(1)
    assert skill.level == 5

    skill.set_XP(273_741)
    assert skill.level == 59
    skill.add_XP(1)
    assert skill.level == 60

    skill.set_XP(13_034_430)
    assert skill.level == 98
    skill.add_XP(1)
    assert skill.level == 99

    skill.set_XP(188_884_739)
    assert skill.level == 125
    skill.add_XP(big_XP)
    assert skill.level == MAX_LEVEL
    assert skill.XP == MAX_XP


def test_loaded_XP():
    skill = Skill('mining', 'gathering', XP=50_000)
    assert skill.level == 42
    assert skill.XP == 50_000

    skill = Skill('mining', 'gathering', XP=big_XP)
    assert skill.level == MAX_LEVEL
    assert skill.XP == MAX_XP


def test_set_level():
    skill = Skill('mining', 'gathering')

    skill.set_level(3)
    assert skill.level == 3
    assert skill.XP == 174

    skill.set_level(1)
    assert skill.level == 1
    assert skill.XP == 0

    skill.set_level(126)
    assert skill.level == 126
    assert skill.XP == 188_884_740
