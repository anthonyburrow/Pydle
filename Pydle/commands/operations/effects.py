from ...util.Command import Command
from ...util.structures.Player import Player
from ...util.structures.UserInterface import UserInterface


def interface_effects(player: Player, ui: UserInterface, command: Command):
    if not command.subcommand and not command.argument:
        return ui.print(str(player.updated_effects), multiline=True)


def detailed_info():
    msg: list = []

    msg.append('Use cases:')
    msg.append('- effects')

    return '\n'.join(msg)
