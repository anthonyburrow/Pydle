import numpy as np

from ..colors import color, COLOR_STATS


MAX_LEVEL: int = 126
MAX_XP: float = 2e8


def level_to_XP(level):
    prev_levels = np.arange(1, level)
    inner = np.floor(prev_levels + 300. * 2.**(prev_levels / 7.))
    XP = int(0.25 * inner.sum())
    return XP


XP_table = {lvl: level_to_XP(lvl) for lvl in range(1, MAX_LEVEL + 1)}


class Stat:

    def __init__(self, name: str):
        self.name: str = name
        self.XP: float = 0.
        self.level: int = 1

    def add_XP(self, amount: float):
        if self.XP >= MAX_XP:
            return

        new_XP = self.XP + amount
        if new_XP < MAX_XP:
            self.XP = new_XP
        else:
            self.XP = MAX_XP

        self._adjust_level()

    def set_XP(self, value):
        self.XP = value

        self._adjust_level()

    def set_level(self, level: int):
        self.level = level
        self.XP = XP_table[level]

    def __str__(self):
        name = color(self.name, COLOR_STATS)
        level = self.level
        xp_to_next = XP_table[level + 1] - self.XP

        msg = f'  {name}: Lvl {level} | {xp_to_next:.0f} EXP to next level'

        return msg

    def _adjust_level(self):
        current_lvl = self.level
        for lvl in range(current_lvl + 1, MAX_LEVEL + 1):
            required_XP = XP_table[lvl]

            if self.XP < required_XP:
                break

            self.level = lvl