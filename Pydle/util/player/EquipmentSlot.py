from enum import Enum, auto


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
