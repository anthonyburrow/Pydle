from ...util.structures.Player import Player
from ...util.structures.UserInterface import UserInterface
from ...util.Result import Result


def interface_tools(player: Player, ui: UserInterface, *args):
    if not args:
        return ui.print(str(player.tools), multiline=True)

    subcommand = args[0]
    tool = ' '.join(args[1:])

    if not tool:
        return ui.print('A tool argument was not given.')

    if subcommand == 'equip':
        result: Result = player.equip_tool(tool)
    elif subcommand == 'unequip':
        result: Result = player.unequip_tool(tool)
    else:
        return ui.print(f'{subcommand} is not a valid argument.')

    ui.print(result.msg)


def detailed_info():
    msg: list = []

    msg.append('Use cases:')
    msg.append('- tools')
    msg.append('- tools equip [tool]')
    msg.append('- tools unequip [tool]')

    return '\n'.join(msg)
