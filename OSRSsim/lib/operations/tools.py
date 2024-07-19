from ...util.structures import Player
from ...util.output import print_output


def interface_tools(player: Player, *args):
    if not args:
        print_output(player.tools)
        return

    subcommand = args[0]
    tool = ' '.join(args[1:])

    if not tool:
        msg = 'A tool argument was not given.'
        print_output(msg)
        return

    if subcommand == 'add':
        operation = player.add_tool(tool)
    elif subcommand == 'remove':
        operation = player.remove_tool(tool)
    else:
        msg = f'{subcommand} is not a valid argument.'
        print_output(msg)
        return

    print_output(operation['msg'])
