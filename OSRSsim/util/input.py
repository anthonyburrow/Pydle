from .commands import *
from ..commands.command_map import map_activity, map_operations, alias_to_command


NULL_INPUT = {
    'type': None
}

COMMAND_PREFIX = '> '


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
    command = alias_to_command(command)

    if command in map_activity:
        return {
            'type': 'activity',
            'activity': map_activity[command]['function'],
            'args': tuple(msg[1:]),
        }
    elif command in map_operations:
        return {
            'type': 'operation',
            'function': map_operations[command]['function'],
            'args': tuple(msg[1:]),
        }
    elif command == CMD_EXIT:
        return {
            'type': 'exit',
        }

    return NULL_INPUT
