from ...util.Command import Command
from ...util.structures.Player import Player
from ...util.structures.UserInterface import UserInterface


def interface_skills(player: Player, ui: UserInterface, command: Command):
    if not command.subcommand and not command.argument:
        return ui.print(str(player.skills), multiline=True)

    try:
        ui.print(player.get_skill(command.argument).details())
    except KeyError:
        ui.print(f'{command.argument} is not a valid skill.')


def detailed_info():
    msg: list = []

    msg.append('Use cases:')
    msg.append('- skills')
    msg.append('- skills [skill]')

    return '\n'.join(msg)
