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

    def __init__(self, player: Player):
        self._player: Player = player

        self._stats: Stats = Stats()

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
            if prev_equippable is not None:
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
        if prev_equippable is None:
            return Result(
                success=False,
                msg=f'{self._player} has no {equippable_key} equipped.'
            )

        self[equippable_key] = None
        self._player.give(prev_equippable.name)

        self._calculate_stats()

        return Result(
            success=True,
            msg=f'{prev_equippable} was unequipped.'
        )

    def get_equippable(self, equippable_key: str) -> Equippable:
        return self[equippable_key]

    def get_equipment(self) -> dict:
        return {equippable_key: self.get_equippable(equippable_key)
                for equippable_key in EQUIPMENT}

    def get_equipment_names(self) -> dict:
        '''Structure for saved profile'''
        equipment_names = {}
        for equippable_key in EQUIPMENT:
            equippable = self.get_equippable(equippable_key)
            if equippable is None:
                equipment_names[equippable_key] = ''
            else:
                equipment_names[equippable_key] = equippable.name

        return equipment_names

    @property
    def stats(self) -> Stats:
        return self._stats

    def load_equipment(self, equipment_names: dict = None):
        for equippable_key, equippable_lib in EQUIPMENT.items():
            # Basically only procs if new player
            if equipment_names is None:
                self[equippable_key] = None
                continue

            # Occurs when there are additions to EQUIPMENT
            if equippable_key not in equipment_names:
                self[equippable_key] = None
                continue

            equippable_name = equipment_names[equippable_key]

            if equippable_name is None or not equippable_name:
                self[equippable_key] = None
                continue

            self[equippable_key] = equippable_lib[equippable_name]

        self._calculate_stats()

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
            equippable_str = equippable if equippable is not None else '---'
            msg.append(f'{name} | {equippable_str}')

        attack_speed_str = self["weapon"].attack_speed if self['weapon'] else 'N/A'
        msg.append(f'\nWeapon tick speed: {attack_speed_str}')

        msg = '\n'.join(msg)

        return msg

    def _calculate_stats(self):
        stats: Stats = Stats()

        for equippable_key, equippable in self.items():
            if equippable is None:
                continue
            stats += equippable.stats

        self._stats = stats
