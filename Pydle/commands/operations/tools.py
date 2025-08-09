from ..Operation import Operation
from ...util.Result import Result
from ...util.items.ItemInstance import ItemInstance
from ...util.items.ItemParser import ITEM_PARSER
from ...util.items.Tool import Tool


class ToolsOperation(Operation):

    name: str = 'tools'
    aliases: list[str] = ['t', 'tool']
    subcommands: list[str] = ['equip', 'unequip']
    help_info: str = "Display and equip the player's tools."

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @classmethod
    def usage(cls) -> str:
        msg: list[str] = []

        msg.append('Use cases:')
        msg.append('- tools')
        msg.append('- tools equip [tool]')
        msg.append('- tools unequip [tool]')

        return '\n'.join(msg)

    def execute(self):
        if not self.command.subcommand and not self.command.argument:
            return self.ui.print(str(self.player.tools), multiline=True)

        if not self.command.argument:
            return self.ui.print('A tool argument was not given.')

        if self.command.quantity != 1:
            return self.ui.print('Only one item can be equipped or unequipped at a time.')

        item_instance: ItemInstance | None = self.command.get_item_instance()

        if not item_instance:
            return self.ui.print(f"Item '{self.command.argument}' is not a valid argument.")

        if not isinstance(item_instance.base, Tool):
            return self.ui.print(f"Item '{item_instance}' is not equippable.")

        if self.command.subcommand == 'equip':
            result: Result = self.player.equip_tool(item_instance)
        elif self.command.subcommand == 'unequip':
            result: Result = self.player.unequip_tool(item_instance)

        self.ui.print(result.msg)
