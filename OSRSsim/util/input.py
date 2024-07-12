from ..lib.command_map import map_activity
from .commands import CMD_EXIT


def flush_input():
    try:
        import msvcrt
        while msvcrt.kbhit():
            msvcrt.getch()
    except ImportError:
        # for linux/unix
        import sys
        import termios
        termios.tcflush(sys.stdin, termios.TCIOFLUSH)


def parse_command(msg: str) -> dict:
    msg = msg.lower()
    msg = msg.split(' ')

    command = msg[0]

    if command in map_activity:
        return {
            'type': 'activity',
            'activity': map_activity[command],
            'args': tuple(msg[1:]),
        }
    elif command == CMD_EXIT:
        return {
            'type': 'exit',
        }
    else:
        return {
            'type': None,
        }
