import numpy as np

from .SkillType import SkillType
from ..colors import color, color_theme


MAX_LEVEL: int = 126
MAX_XP: float = 2e8


def level_to_xp(level):
    prev_levels = np.arange(1, level)
    inner = np.floor(prev_levels + 300. * 2.**(prev_levels / 7.))
    xp = int(0.25 * inner.sum())
    return xp


XP_TABLE = {lvl: level_to_xp(lvl) for lvl in range(1, MAX_LEVEL + 1)}


class Skill:

    def __init__(self, skill_type: SkillType, skill_category: str, xp: float = 0.):
        self.skill_type: SkillType = skill_type
        self.skill_category: str = skill_category

        self.xp: float = 0.
        self.level: int = 1
        if xp > 0.:
            self.set_xp(xp)

    def add_xp(self, amount: float) -> dict:
        if self.xp >= MAX_XP:
            return

        new_xp = self.xp + amount
        if new_xp < MAX_XP:
            self.xp = new_xp
        else:
            self.xp = MAX_XP

        return self._adjust_level()

    def set_xp(self, value: float):
        if value > MAX_XP:
            value = MAX_XP
        self.xp = value

        self._adjust_level()

    def set_level(self, level: int):
        self.level = level
        self.xp = XP_TABLE[level]

    def details(self) -> str:
        level = self.level
        if level >= 99:
            level = color(level, color_theme['skill_lvl99'])

        msg = f'{str(self)}: Lvl {level}'

        if level < MAX_LEVEL:
            xp_to_next = XP_TABLE[level + 1] - self.xp
            msg = f'{msg} | {xp_to_next:.0f} EXP to next level'
        else:
            msg = f'{msg} | {self.xp:.0f} EXP'

        return msg

    def __str__(self) -> str:
        return color(self.skill_type, color_theme[f'skill_{self.skill_category}'])

    def _adjust_level(self) -> dict[str, bool]:
        current_lvl: int = self.level
        leveled_up: bool = False
        for lvl in range(current_lvl + 1, MAX_LEVEL + 1):
            required_xp = XP_TABLE[lvl]

            if self.xp < required_xp:
                break

            self.level = lvl

            leveled_up = True

        return {
            'leveled_up': leveled_up,
        }
