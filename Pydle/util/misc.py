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
    import Xlib


def is_display_available() -> bool:
    if SYS_PLATFORM == Platform.WINDOWS:
        return True
    elif SYS_PLATFORM == Platform.LINUX:
        try:
            d = Xlib.display.Display()
            d.close()
            return True
        except Xlib.error.DisplayNameError:
            return False
    return False


def get_client_ID():
    if SYS_PLATFORM == Platform.WINDOWS:
        return win32gui.GetForegroundWindow()
    elif SYS_PLATFORM == Platform.LINUX:
        d = Xlib.display.Display()
        window = d.get_input_focus().focus
        return window.id

def client_focused(client_ID) -> bool:
    if not is_display_available():
        return True

    return client_ID == get_client_ID()
