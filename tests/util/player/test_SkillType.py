import pytest

from Pydle.util.player.SkillType import SkillType


def test_enum_members_exist_and_order():
    expected = [
        'HITPOINTS', 'STRENGTH', 'DEFENSE', 'MAGIC', 'BARRIER', 'ACCURACY', 'EVASIVENESS',
        'FISHING', 'FORAGING', 'MINING', 'WOODCUTTING',
        'COOKING', 'CRAFTING', 'HERBLORE', 'SMITHING'
    ]
    assert [m.name for m in SkillType] == expected


@pytest.mark.parametrize('skill_type,expected_str', [
    (SkillType.HITPOINTS, 'Hitpoints'),
    (SkillType.STRENGTH, 'Strength'),
    (SkillType.WOODCUTTING, 'Woodcutting'),
    (SkillType.HERBLORE, 'Herblore'),
])
def test_str_returns_title_case(skill_type, expected_str):
    assert str(skill_type) == expected_str


@pytest.mark.parametrize('input_str,expected_enum', [
    ('hitpoints', SkillType.HITPOINTS),
    ('HITPOINTS', SkillType.HITPOINTS),
    ('Hitpoints', SkillType.HITPOINTS),
    ('fishing', SkillType.FISHING),
    ('CRAFTING', SkillType.CRAFTING),
])
def test_from_string_valid(input_str, expected_enum):
    assert SkillType.from_string(input_str) == expected_enum


@pytest.mark.parametrize('invalid_input', [
    'hitpoint',     # missing 's'
    'combat',       # not a skill
    '',             # empty
    '123',          # numbers
    'wood cutting'  # has space
])
def test_from_string_invalid(invalid_input):
    with pytest.raises(ValueError):
        SkillType.from_string(invalid_input)


def test_enum_auto_values_unique():
    values = [e.value for e in SkillType]
    assert len(values) == len(set(values)), 'Duplicate auto() values detected'
