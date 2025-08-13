import pytest

from Pydle.util.player.EquipmentSlot import EquipmentSlot


def test_enum_members_exist():
    expected = [
        'WEAPON', 'OFFHAND', 'HELM', 'BODY',
        'LEGS', 'GLOVES', 'BOOTS'
    ]
    assert [e.name for e in EquipmentSlot] == expected


def test_enum_auto_values_unique():
    values = [e.value for e in EquipmentSlot]
    assert len(values) == len(set(values)), 'Enum auto() assigned duplicate values'


@pytest.mark.parametrize('slot,expected_str', [
    (EquipmentSlot.WEAPON, 'Weapon'),
    (EquipmentSlot.OFFHAND, 'Offhand'),
    (EquipmentSlot.HELM, 'Helm'),
    (EquipmentSlot.BODY, 'Body'),
    (EquipmentSlot.LEGS, 'Legs'),
    (EquipmentSlot.GLOVES, 'Gloves'),
    (EquipmentSlot.BOOTS, 'Boots'),
])
def test_str_returns_title_case(slot, expected_str):
    assert str(slot) == expected_str


def test_enum_iterable_order():
    members = list(EquipmentSlot)
    assert members[0] == EquipmentSlot.WEAPON
    assert members[-1] == EquipmentSlot.BOOTS


@pytest.mark.parametrize('invalid_name', [
    'SWORD', 'shield', 'helmet', '', '123'
])
def test_invalid_lookup_by_name(invalid_name):
    with pytest.raises(KeyError):
        EquipmentSlot[invalid_name]


@pytest.mark.parametrize('invalid_value', [
    999, -1, None, 'Weapon', object()
])
def test_invalid_lookup_by_value(invalid_value):
    with pytest.raises(ValueError):
        EquipmentSlot(invalid_value)