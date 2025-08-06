from ...util.Command import Command
from ...util.structures.Player import Player
from ...util.structures.UserInterface import UserInterface


def interface_bank(player: Player, ui: UserInterface, command: Command):
    if not command.subcommand and not command.argument:
        return ui.print(str(player.bank), multiline=True)


def detailed_info():
    msg: list = []

    msg.append('Use cases:')
    msg.append('- bank')

    return '\n'.join(msg)
