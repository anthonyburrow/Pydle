from .commands import *
from ..lib.command_map import map_activity, map_info, map_testing


NULL_INPUT = {
    'type': None
}


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
    elif command in map_info:
        return {
            'type': 'info',
            'function': map_info[command],
        }
    elif command == CMD_TESTING:
        try:
            func = map_testing[msg[1]]
        except IndexError:
            return NULL_INPUT
        return {
            'type': 'testing',
            'function': func,
        }
    elif command == CMD_EXIT:
        return {
            'type': 'exit',
        }

    return NULL_INPUT
