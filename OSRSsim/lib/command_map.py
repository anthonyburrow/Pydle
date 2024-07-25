from .activities import skilling

from .operations.bank import interface_bank
from .operations.skills import interface_skills
from .operations.tools import interface_tools
from .operations.testing import interface_testing

from ..util.output import print_info
from ..util.colors import color, color_theme


def interface_help(*args):
    msg: list = []

    msg.append('Operations:')
    for command, command_info in map_operations.items():
        if command == 'testing':
            continue

        alias_str = ''
        if 'aliases' in command_info:
            alias_str = [color(cmd, color_theme['UI_1'])
                         for cmd in command_info['aliases']]
            alias_str = ', '.join(alias_str)
            alias_str = f"({alias_str}) "

        command_str = color(command, color_theme['UI_1'])
        msg.append(f"  - {command_str} {alias_str}: {command_info['help_info']}")

        for use in command_info['use_case']:
            msg.append(f'    {use}')

    msg.append('')
    msg.append('Activities:')
    for command, command_info in map_activity.items():
        alias_str = ''
        if 'aliases' in command_info:
            alias_str = [color(cmd, color_theme['UI_1'])
                         for cmd in command_info['aliases']]
            alias_str = ', '.join(alias_str)
            alias_str = f"({alias_str}) "

        command_str = color(command, color_theme['UI_1'])
        msg.append(f"  - {command_str} {alias_str}: {command_info['help_info']}")

        for use in command_info['use_case']:
            msg.append(f'    {use}')

    print_info('\n'.join(msg), multiline=True)


# Mapping
map_activity = {
    'mine': {
        'function': skilling.MiningActivity,
        'help_info': 'Begin a mining trip.',
        'use_case': ('mine [ore]',),
    },
    'chop': {
        'function': skilling.WoodcuttingActivity,
        'help_info': 'Begin a woodcutting trip.',
        'use_case': ('chop [log]',),
    },
    'collect': {
        'function': skilling.ForagingActivity,
        'help_info': 'Begin a foraging trip.',
        'use_case': ('collect [herb]',),
    },
}

map_operations = {
    'bank': {
        'function': interface_bank,
        'aliases': ('b',),
        'help_info': "Display the player's bank.",
        'use_case': ('bank',),
    },
    'help': {
        'function': interface_help,
        'aliases': ('?', 'h'),
        'help_info': 'Show the list of available commands.',
        'use_case': ('help',),
    },
    'skills': {
        'function': interface_skills,
        'aliases': ('s', 'skill'),
        'help_info': "Display the player's skills.",
        'use_case': ('skills', 'skills [skill]'),
    },
    'testing': {
        'function': interface_testing,
        'aliases': ('test',),
        'help_info': 'Non-production testing commands.',
        'use_case': ('testing skilling',),
    },
    'tools': {
        'function': interface_tools,
        'aliases': ('t', 'tool'),
        'help_info': "Display the player's tools.",
        'use_case': ('tools', 'tools add [tool]', 'tools remove [tool]'),
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
