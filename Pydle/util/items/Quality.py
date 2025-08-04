from enum import Enum


class Quality(Enum):
    NONE = 0
    POOR = 1
    GOOD = 2
    GREAT = 3
    SUPERIOR = 4
    MASTER = 5

    @classmethod
    def from_value(cls, value: int):
        if value is None:
            return None
        return cls(value)

    def __str__(self) -> str:
        return self.name.title()
