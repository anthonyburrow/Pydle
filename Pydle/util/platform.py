import sys
from enum import Enum, auto


class Platform(Enum):
    WINDOWS = auto()
    LINUX = auto()
    MACOS = auto()
    UNKNOWN = auto()


def get_platform() -> Platform:
    if sys.platform.startswith('win'):
        return Platform.WINDOWS
    elif sys.platform.startswith('linux'):
        return Platform.LINUX
    elif sys.platform.startswith('darwin'):
        return Platform.MACOS
    else:
        return Platform.UNKNOWN


SYS_PLATFORM: Platform = get_platform()
