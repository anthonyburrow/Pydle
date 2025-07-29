from . import Player, Equippable
from .Stats import Stats
from ..colors import color
from ..Result import Result
from ...lib.equipment import (
    WEAPONS,
    OFFHANDS,
    HELMS,
    BODIES,
    LEGS,
    GLOVES,
    BOOTS,
)


EQUIPMENT = {
    'weapon': WEAPONS,
    'offhand': OFFHANDS,
    'helm': HELMS,
    'body': BODIES,
    'legs': LEGS,
    'gloves': GLOVES,
    'boots': BOOTS,
}


class Equipment(dict):

    def __init__(self, player: Player, equipment_dict: dict = None):
        self._player: Player = player

        self._stats: Stats = Stats()

        equipment_dict = equipment_dict or {}

        for equippable_key, equippable_lib in EQUIPMENT.items():
            equippable_name: str = equipment_dict.get(equippable_key, '')
            self[equippable_key] = equippable_lib.get(equippable_name, '')

        self._calculate_stats()

    def equip(self, equippable_name: str) -> Result:
        if not self._player.has(equippable_name):
            return Result(
                success=False,
                msg=f'{self._player} does not have a {equippable_name}.'
            )

        for equippable_key, equippable_lib in EQUIPMENT.items():
            if equippable_name not in equippable_lib:
                continue

            prev_equippable: Equippable = self.get_equippable(equippable_key)
            if prev_equippable:
                self._player.give(prev_equippable.name)

            self._player.remove(equippable_name, quantity=1)
            equippable = equippable_lib[equippable_name]
            self[equippable_key] = equippable

            self._calculate_stats()

            return Result(
                success=True,
                msg=f'{equippable} was equipped.'
            )

        return Result(
            success=False,
            msg=f'{equippable_name.capitalize()} cannot be equipped.'
        )

    def unequip(self, equippable_key: str) -> Result:
        if equippable_key not in self:
            return Result(
                success=False,
                msg=f'{equippable_key.capitalize()} is not a valid type of equipment (helm, body, etc.).',
            )

        prev_equippable: Equippable = self.get_equippable(equippable_key)
        if not prev_equippable:
            return Result(
                success=False,
                msg=f'{self._player} has no {equippable_key} equipped.'
            )

        self[equippable_key] = ''
        self._player.give(prev_equippable.name)

        self._calculate_stats()

        return Result(
            success=True,
            msg=f'{prev_equippable} was unequipped.'
        )

    def get_equippable(self, equippable_key: str) -> Equippable:
        return self[equippable_key]

    def get_equipment(self) -> dict:
        return {
            equippable_key: self.get_equippable(equippable_key)
            for equippable_key in EQUIPMENT
        }

    def to_dict(self) -> dict:
        equipment_names: dict = {}

        for equippable_key in EQUIPMENT:
            equippable: Equippable = self.get_equippable(equippable_key)
            equipment_names[equippable_key] = equippable.name if equippable else ''

        return equipment_names

    @property
    def stats(self) -> Stats:
        return self._stats

    def _calculate_stats(self):
        self._stats.reset()

        for equippable_key, equippable in self.items():
            if not equippable:
                continue
            self._stats += equippable.stats

    def __str__(self) -> str:
        msg: list = []
        just_amount: int = max([len(e) for e in EQUIPMENT])
        for equippable_key in EQUIPMENT:
            equippable: Equippable = self.get_equippable(equippable_key)
            name = color(
                equippable_key.capitalize(),
                '',
                justify=just_amount
            )
            equippable_str = equippable if equippable else '---'
            msg.append(f'{name} | {equippable_str}')

        attack_speed_str = self['weapon'].attack_speed if self['weapon'] else 'N/A'
        msg.append(f'\nWeapon tick speed: {attack_speed_str}')

        msg = '\n'.join(msg)

        return msg
