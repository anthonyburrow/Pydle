from enum import Enum, auto
from typing import Self


class Quality(Enum):
    POOR = auto()
    GOOD = auto()
    GREAT = auto()
    SUPERIOR = auto()
    MASTER = auto()

    @classmethod
    def from_value(cls, value: int | None) -> Self | None:
        if value is None:
            return None
        return cls(value)

    def __str__(self) -> str:
        return self.name
