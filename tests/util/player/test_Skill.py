from Pydle.util.player.Skill import Skill, ExpGainResult, MAX_XP, MAX_LEVEL
from Pydle.util.player.SkillType import SkillType


BIG_XP = 100_000_000_000


def test_leveling():
    skill = Skill(SkillType.MINING, 'gathering')

    skill.add_xp(82)
    assert skill.level == 1
    skill.add_xp(1)
    assert skill.level == 2

    skill.set_xp(276)
    assert skill.level == 4
    skill.add_xp(111)
    assert skill.level == 4
    skill.add_xp(1)
    assert skill.level == 5

    skill.set_xp(273_741)
    assert skill.level == 59
    skill.add_xp(1)
    assert skill.level == 60

    skill.set_xp(13_034_430)
    assert skill.level == 98
    skill.add_xp(1)
    assert skill.level == 99

    skill.set_xp(188_884_739)
    assert skill.level == 125
    skill.add_xp(BIG_XP)
    assert skill.level == MAX_LEVEL
    assert skill.xp == MAX_XP


def test_loaded_xp():
    skill = Skill(SkillType.MINING, 'gathering', xp=50_000)
    assert skill.level == 42
    assert skill.xp == 50_000

    skill = Skill(SkillType.MINING, 'gathering', xp=BIG_XP)
    assert skill.level == MAX_LEVEL
    assert skill.xp == MAX_XP


def test_set_level():
    skill = Skill(SkillType.MINING, 'gathering')

    skill.set_level(3)
    assert skill.level == 3
    assert skill.xp == 174

    skill.set_level(1)
    assert skill.level == 1
    assert skill.xp == 0

    skill.set_level(126)
    assert skill.level == 126
    assert skill.xp == 188_884_740


def test_add_xp_returns_exp_gain_result():
    skill = Skill(SkillType.MINING, 'gathering')

    result = skill.add_xp(83)

    assert isinstance(result, ExpGainResult)
    assert result.leveled_up
