from enum import Enum, auto
from typing import Self

class SkillType(Enum):
    # Combat skills
    HITPOINTS = auto()
    STRENGTH = auto()
    DEFENSE = auto()
    MAGIC = auto()
    BARRIER = auto()
    ACCURACY = auto()
    EVASIVENESS = auto()
    # Gathering skills
    FISHING = auto()
    FORAGING = auto()
    MINING = auto()
    WOODCUTTING = auto()
    # Artisan skills
    COOKING = auto()
    CRAFTING = auto()
    HERBLORE = auto()
    SMITHING = auto()

    @classmethod
    def from_string(cls, skill_name: str) -> Self:
        try:
            return cls[skill_name.upper()]
        except KeyError:
            raise ValueError(f"Invalid skill type name: '{skill_name}'")

    def __str__(self):
        return self.name.title()