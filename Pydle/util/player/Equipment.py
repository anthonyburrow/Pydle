from enum import Enum, auto
from typing import Self

from .Player import Player
from .Stats import Stats
from ..Result import Result
from ..visuals import centered_title
from ..items.ItemInstance import ItemInstance


class EquipmentSlot(Enum):
    WEAPON = auto()
    OFFHAND = auto()
    HELM = auto()
    BODY = auto()
    LEGS = auto()
    GLOVES = auto()
    BOOTS = auto()

    def __str__(self) -> str:
        return self.name.title()


class Equipment(dict):

    def __init__(self, player: Player, equipment_dict: dict | None = None):
        self._player: Player = player

        self._stats: Stats = Stats()

        equipment_dict = equipment_dict or {}
        self.load_from_dict(equipment_dict)

    def equip(self, item_instance: ItemInstance) -> Result:
        if not self._player.has(item_instance):
            return Result(
                success=False,
                msg=f'{self._player} does not have a {item_instance}.'
            )

        equipment_slot: EquipmentSlot = item_instance.equipment_slot

        previous_instance: ItemInstance | None = self.get(equipment_slot)
        if previous_instance:
            self._player.give(previous_instance)

        self._player.remove(item_instance)
        self[equipment_slot] = item_instance

        self._calculate_stats()

        return Result(
            success=True,
            msg=f'{item_instance} was equipped.'
        )

    def unequip(self, item_instance: ItemInstance) -> Result:
        equipment_slot: EquipmentSlot = item_instance.equipment_slot

        previous_instance: ItemInstance | None = self.get(equipment_slot)
        if not previous_instance or previous_instance != item_instance:
            return Result(
                success=False,
                msg=f'{self._player} does not have {item_instance} equipped.'
            )

        self[equipment_slot] = None
        self._player.give(item_instance)

        self._calculate_stats()

        return Result(
            success=True,
            msg=f'{previous_instance} was unequipped.'
        )

    def to_dict(self) -> dict[str, dict | None]:
        equipment_dict: dict[str, dict | None] = {}

        for equipment_slot, item_instance in self.items():
            if not item_instance:
                equipment_dict[equipment_slot.name] = None
                continue
            equipment_dict[equipment_slot.name] = item_instance.to_dict()

        return equipment_dict

    def load_from_dict(self, equipment_dict: dict) -> None:
        for equipment_slot in EquipmentSlot:
            instance_dict: dict | None = equipment_dict.get(equipment_slot.name)

            if instance_dict is None:
                self[equipment_slot] = None
                continue

            item_instance: ItemInstance = ItemInstance.from_dict(instance_dict)
            self[equipment_slot] = item_instance

        self._calculate_stats()

    @property
    def stats(self) -> Stats:
        return self._stats

    def _calculate_stats(self):
        self._stats.reset()

        for equippable_slot, item_instance in self.items():
            if not item_instance:
                continue
            self._stats += item_instance.stats

    def __str__(self) -> str:
        msg: list = []

        max_type_length: int = max([len(str(x)) for x in EquipmentSlot])
        max_equippable_length: int = 0
        for item_instance in self.values():
            if item_instance is None:
                length = 3
            else:
                length = len(item_instance.name)
            if length > max_equippable_length:
                max_equippable_length = length
        total_length = max_type_length + max_equippable_length + 3

        msg.append(centered_title('EQUIPMENT', total_length))

        for equippable_slot, item_instance in self.items():
            equippable_str = item_instance or '---'
            msg.append(f'{equippable_slot:>{max_type_length}} | {equippable_str}')

        weapon_instance: ItemInstance | None = self.get(EquipmentSlot.WEAPON)
        attack_speed_str = weapon_instance.attack_speed if weapon_instance else 'N/A'
        msg.append(f'\nWeapon tick speed: {attack_speed_str}')

        msg = '\n'.join(msg)

        return msg

    def __setitem__(self, key, value):
        if key not in EquipmentSlot:
            raise KeyError(f'Invalid EquipmentSlot key: "{key}"')
        super().__setitem__(key, value)
