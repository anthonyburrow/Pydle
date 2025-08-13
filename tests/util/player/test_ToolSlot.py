import pytest

from Pydle.util.player.ToolSlot import ToolSlot


def test_enum_members_exist():
    expected = ['PICKAXE', 'AXE', 'SECATEURS', 'FISHING_ROD']
    assert [e.name for e in ToolSlot] == expected


def test_enum_auto_values_unique():
    values = [e.value for e in ToolSlot]
    assert len(values) == len(set(values)), 'Enum auto() assigned duplicate values'


@pytest.mark.parametrize('slot,expected_str', [
    (ToolSlot.PICKAXE, 'Pickaxe'),
    (ToolSlot.AXE, 'Axe'),
    (ToolSlot.SECATEURS, 'Secateurs'),
    (ToolSlot.FISHING_ROD, 'Fishing Rod'),
])
def test_str_returns_title_case_with_spaces(slot, expected_str):
    assert str(slot) == expected_str


def test_enum_iterable_order():
    members = list(ToolSlot)
    assert members[0] == ToolSlot.PICKAXE
    assert members[-1] == ToolSlot.FISHING_ROD


@pytest.mark.parametrize('invalid_name', [
    'PICK', 'rod', 'fishingrod', 'AX', '', '123'
])
def test_invalid_lookup_by_name(invalid_name):
    with pytest.raises(KeyError):
        ToolSlot[invalid_name]


@pytest.mark.parametrize('invalid_value', [
    999, -1, None, 'Pickaxe', object()
])
def test_invalid_lookup_by_value(invalid_value):
    with pytest.raises(ValueError):
        ToolSlot(invalid_value)
