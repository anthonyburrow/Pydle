from enum import Enum, auto


class ToolSlot(Enum):
    PICKAXE = auto()
    AXE = auto()
    SECATEURS = auto()
    FISHING_ROD = auto()

    def __str__(self) -> str:
        return self.name.replace('_', ' ').title()
