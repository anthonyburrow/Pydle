from ...util.Result import Result
from ...util.Command import Command
from ...util.ItemParser import ITEM_PARSER
from ...util.items.Item import ItemInstance
from ...util.items.Tool import Tool
from ...util.structures.Player import Player
from ...util.structures.UserInterface import UserInterface


def interface_tools(player: Player, ui: UserInterface, command: Command):
    if not command.subcommand and not command.item_name:
        return ui.print(str(player.tools), multiline=True)

    if not command.item_name:
        return ui.print('A tool argument was not given.')

    if command.quantity != 1:
        return ui.print('Only one item can be equipped or unequipped at a time.')

    item_instance: ItemInstance | None = ITEM_PARSER.get_instance(command)

    if not item_instance:
        return ui.print(f"Item '{command.item_name}' is not a valid argument.")

    if not isinstance(item_instance.base, Tool):
        return ui.print(f"Item '{item_instance}' is not equippable.")

    if command.subcommand == 'equip':
        result: Result = player.equip_tool(item_instance)
    elif command.subcommand == 'unequip':
        result: Result = player.unequip_tool(item_instance)

    ui.print(result.msg)


def detailed_info():
    msg: list = []

    msg.append('Use cases:')
    msg.append('- tools')
    msg.append('- tools equip [tool]')
    msg.append('- tools unequip [tool]')

    return '\n'.join(msg)
