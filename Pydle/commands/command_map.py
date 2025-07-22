from .activities import combat
from .activities import skilling

from .operations import bank
from .operations import effects
from .operations import equipment
from .operations import skills
from .operations import tools
from .operations import testing

from ..util.output import print_info
from ..util.colors import color, color_theme
from ..util.structures.Player import Player
from ..util.commands import *


def interface_help(player: Player, *args):
    if args:
        subcommand = args[0]
        if subcommand in map_activity:
            msg_func = map_activity[subcommand]['detailed_info']
            msg = msg_func()
            print_info(msg, multiline=True)
        elif subcommand in map_operations:
            msg_func = map_operations[subcommand]['detailed_info']
            msg = msg_func()
            print_info(msg, multiline=True)
        elif subcommand == 'help':
            command_str = color('help', color_theme['UI_1'])
            msg = f'Use `{command_str} [command]` for more detail on a command.'
            print_info(msg)
        else:
            msg = f'Invalid argument {subcommand}.'
            print_info(msg)

        return

    msg: list = []

    command_str = color('help', color_theme['UI_1'])
    msg.append(f'Use `{command_str} [command]` for more detail on a command.')

    msg.append('')
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

    msg.append('')
    msg.append('Other:')

    command_str = color(KEY_CANCEL, color_theme['UI_1'])
    msg.append(f'  - Hold "{command_str}" to cancel an ongoing activity.')

    command_str = color(CMD_EXIT, color_theme['UI_1'])
    msg.append(f'  - {command_str}: Exit the game.')

    print_info('\n'.join(msg), multiline=True)


# Mapping
map_activity = {
    'chop': {
        'function': skilling.WoodcuttingActivity,
        'help_info': 'Begin a woodcutting trip.',
        'detailed_info': skilling.woodcutting.detailed_info,
    },
    'clean': {
        'function': skilling.CleaningActivity,
        'help_info': 'Begin to clean herbs.',
        'detailed_info': skilling.cleaning.detailed_info,
    },
    'collect': {
        'function': skilling.ForagingActivity,
        'help_info': 'Begin to forage for herbs.',
        'detailed_info': skilling.foraging.detailed_info,
    },
    'cook': {
        'function': skilling.CookingActivity,
        'help_info': 'Begin to cook food.',
        'detailed_info': skilling.cooking.detailed_info,
    },
    'craft': {
        'function': skilling.CraftingActivity,
        'help_info': 'Begin to craft items.',
        'detailed_info': skilling.crafting.detailed_info,
    },
    'fish': {
        'function': skilling.FishingActivity,
        'help_info': 'Begin to fish.',
        'detailed_info': skilling.fishing.detailed_info,
    },
    'kill': {
        'function': combat.KillingActivity,
        'help_info': 'Begin to kill a monster.',
        'detailed_info': combat.killing.detailed_info,
    },
    'mine': {
        'function': skilling.MiningActivity,
        'help_info': 'Begin to mine ore.',
        'detailed_info': skilling.mining.detailed_info,
    },
    'mix': {
        'function': skilling.MixingActivity,
        'help_info': 'Begin to mix a potion.',
        'detailed_info': skilling.mixing.detailed_info,
    },
    'smelt': {
        'function': skilling.SmeltingActivity,
        'help_info': 'Begin to smelt an ore.',
        'detailed_info': skilling.smelting.detailed_info,
    },
    'smith': {
        'function': skilling.SmithingActivity,
        'help_info': 'Begin to smith a metal item.',
        'detailed_info': skilling.smithing.detailed_info,
    },
}

map_operations = {
    'bank': {
        'function': bank.interface_bank,
        'aliases': ('b',),
        'help_info': "Display the player's bank.",
        'detailed_info': bank.detailed_info,
    },
    'effects': {
        'function': effects.interface_effects,
        'aliases': ('effect',),
        'help_info': "Display and equip the player's ongoing effects.",
        'detailed_info': effects.detailed_info,
    },
    'equipment': {
        'function': equipment.interface_equipment,
        'aliases': ('e', 'equip'),
        'help_info': "Display and equip the player's equipment.",
        'detailed_info': equipment.detailed_info,
    },
    'help': {
        'function': interface_help,
        'aliases': ('?', 'h'),
        'help_info': 'Show the list of available commands.',
    },
    'skills': {
        'function': skills.interface_skills,
        'aliases': ('s', 'skill'),
        'help_info': "Display the player's skills.",
        'detailed_info': skills.detailed_info,
    },
    'testing': {
        'function': testing.interface_testing,
        'aliases': ('test',),
        'help_info': 'Non-production testing commands.',
        'detailed_info': testing.detailed_info,
    },
    'tools': {
        'function': tools.interface_tools,
        'aliases': ('t', 'tool'),
        'help_info': "Display and equip the player's tools.",
        'detailed_info': tools.detailed_info,
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
