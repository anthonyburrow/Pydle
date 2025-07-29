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


SYS_PLATFORM = get_platform()


if SYS_PLATFORM == Platform.WINDOWS:
    import win32gui
elif SYS_PLATFORM == Platform.LINUX:
    import shutil
    import subprocess


def get_client_ID():
    if SYS_PLATFORM == Platform.WINDOWS:
        return win32gui.GetForegroundWindow()
    elif SYS_PLATFORM == Platform.LINUX:
        result = subprocess.run(
            ['xdotool', 'getwindowfocus'],
            stdout=subprocess.PIPE,
            stderr=subprocess.DEVNULL,
            text=True
        )
        return result.stdout.strip()

def client_focused(client_ID) -> bool:
    return client_ID == get_client_ID()
