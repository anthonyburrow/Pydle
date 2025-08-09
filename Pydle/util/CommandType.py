from enum import Enum, auto


class CommandType(Enum):
    UNKNOWN = auto()
    OPERATION = auto()
    ACTIVITY = auto()
    EXIT = auto()