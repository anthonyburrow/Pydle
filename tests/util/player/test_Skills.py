import pytest

from Pydle.util.player.Skill import Skill
from Pydle.util.player.Skills import Skills, SKILLS
from Pydle.util.player.SkillType import SkillType


def test_init_default_values():
    skills: Skills = Skills()

    assert set(skills.keys()) == set(SKILLS.keys())

    for skill in skills.values():
        assert isinstance(skill, Skill)
        assert skill.xp == 0.


def test_init_with_values():
    initial_xp: dict[str, float] = {'FISHING': 150., 'STRENGTH': 500.}
    skills: Skills = Skills(initial_xp)

    assert skills[SkillType.FISHING].xp == 150.
    assert skills[SkillType.STRENGTH].xp == 500.

    for key in SKILLS:
        if key.name not in initial_xp:
            assert skills[key].xp == 0.


def test_get_skill_returns_correct_instance():
    skills: Skills = Skills()
    fishing: Skill = skills[SkillType.FISHING]

    assert isinstance(fishing, Skill)
    assert fishing.skill_type == SkillType.FISHING


def test_add_xp_and_get_level():
    skills: Skills = Skills()
    starting_level: int = skills.get_level(SkillType.FISHING)
    skills.add_xp(SkillType.FISHING, 5000.)

    assert skills[SkillType.FISHING].level >= starting_level


def test_set_xp_changes_value():
    skills: Skills = Skills()
    skills.set_xp(SkillType.FISHING, 1234.5)

    assert skills[SkillType.FISHING].xp == 1234.5


def test_set_level_sets_correct_level():
    skills: Skills = Skills()
    skills.set_level(SkillType.FISHING, 10)

    assert skills.get_level(SkillType.FISHING) == 10


def test_to_dict_matches_xp_values():
    initial_xp: dict[str, float] = {'FISHING': 200., 'STRENGTH': 300.}
    skills: Skills = Skills(initial_xp)
    skills_dict: dict[str, float] = skills.to_dict()

    assert skills_dict['FISHING'] == 200.
    assert skills_dict['STRENGTH'] == 300.


def test_setitem_invalid_key():
    skills: Skills = Skills()
    with pytest.raises(KeyError):
        _ = skills['invalid_skill']
