from ...util.structures.Player import Player
from ...util.structures.UserInterface import UserInterface
from ...util.Result import Result


def interface_equipment(player: Player, ui: UserInterface, *args):
    if not args:
        return ui.print(str(player.equipment), multiline=True)

    subcommand = args[0]

    if subcommand == 'stats':
        return ui.print(str(player.stats), multiline=True)

    equippable_name = ' '.join(args[1:])

    if not equippable_name:
        return ui.print('An item argument was not given.')

    if subcommand == 'equip':
        result: Result = player.equip(equippable_name)
    elif subcommand == 'unequip':
        result: Result = player.unequip(equippable_name)
    else:
        return ui.print(f'"{subcommand}" is not a valid argument.')

    ui.print(result.msg)


def detailed_info():
    msg: list = []

    msg.append('Use cases:')
    msg.append('- equipment')
    msg.append('- equipment equip [item]')
    msg.append('- equipment unequip[item]')
    msg.append('- equipment stats')

    return '\n'.join(msg)
