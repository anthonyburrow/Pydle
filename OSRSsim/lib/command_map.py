from .activities import skilling

from .operations.bank import interface_bank
from .operations.skills import interface_skills
from .operations.tools import interface_tools
from .operations.testing import interface_testing

from ..util.output import print_info
from ..util.colors import color, COLOR_UI_1


def interface_help(*args):
    msg: list = []

    msg.append('Operations:')
    for command, command_info in map_operations.items():
        if command == 'testing':
            continue

        alias_str = ''
        if 'aliases' in command_info:
            alias_str = [color(cmd, COLOR_UI_1)
                         for cmd in command_info['aliases']]
            alias_str = ', '.join(alias_str)
            alias_str = f"({alias_str}) "

        command_str = color(command, COLOR_UI_1)
        msg.append(f"  {command_str} {alias_str}: {command_info['help_info']}")

    msg.append('')
    msg.append('Activities:')
    for command, command_info in map_activity.items():
        alias_str = ''
        if 'aliases' in command_info:
            alias_str = [color(cmd, COLOR_UI_1)
                         for cmd in command_info['aliases']]
            alias_str = ', '.join(alias_str)
            alias_str = f"({alias_str}) "

        command_str = color(command, COLOR_UI_1)
        msg.append(f"  {command_str} {alias_str}: {command_info['help_info']}")

    print_info('\n'.join(msg), multiline=True)


# Mapping
map_activity = {
    'mine': {
        'function': skilling.MiningActivity,
        'help_info': 'Begin a mining trip.',
    },
    'chop': {
        'function': skilling.WoodcuttingActivity,
        'help_info': 'Begin a woodcutting trip.',
    },
    'collect': {
        'function': skilling.ForagingActivity,
        'help_info': 'Begin a foraging trip.',
    },
}

map_operations = {
    'bank': {
        'function': interface_bank,
        'aliases': ('b',),
        'help_info': "Display the player's bank.",
    },
    'help': {
        'function': interface_help,
        'aliases': ('?', 'h'),
        'help_info': 'Show the list of available commands.',
    },
    'skills': {
        'function': interface_skills,
        'aliases': ('s', 'skill'),
        'help_info': "Display the player's skills.",
    },
    'testing': {
        'function': interface_testing,
        'aliases': ('test',),
        'help_info': 'Non-production testing commands.',
    },
    'tools': {
        'function': interface_tools,
        'aliases': ('t', 'tool'),
        'help_info': "Display the player's tools.",
    },
}


# Aliases
def populate_aliases(map_dict: dict) -> dict:
    alias_map = {}
    for command in map_dict:
        if 'aliases' not in map_dict[command]:
            continue
        aliases = map_dict[command]['aliases']
        for alias in aliases:
            alias_map[alias] = command
    return alias_map


alias_activity = populate_aliases(map_activity)
alias_operations = populate_aliases(map_operations)


def alias_to_command(alias: str):
    if alias in alias_activity:
        command = alias_activity[alias]
    elif alias in alias_operations:
        command = alias_operations[alias]
    else:
        command = alias

    return command
