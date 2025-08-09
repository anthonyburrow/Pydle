from ...util.Result import Result
from ...util.items.Equippable import Equippable
from ...util.items.ItemInstance import ItemInstance
from ...util.structures.Operation import Operation


class EquipmentOperation(Operation):

    name: str = 'equipment'
    aliases: list[str] = ['e', 'equip']
    subcommands: list[str] = ['equip', 'unequip', 'stats']
    help_info: str = "Display and equip the player's equipment."

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @classmethod
    def usage(cls) -> str:
        msg: list[str] = []

        msg.append('Use cases:')
        msg.append('- equipment')
        msg.append('- equipment equip [item]')
        msg.append('- equipment unequip[item]')
        msg.append('- equipment stats')

        return '\n'.join(msg)

    def execute(self):
        if not self.command.subcommand and not self.command.argument:
            return self.ui.print(str(self.player.equipment), multiline=True)

        if self.command.subcommand == 'stats':
            return self.ui.print(str(self.player.stats), multiline=True)

        if not self.command.argument:
            return self.ui.print('An item argument was not given.')

        if self.command.quantity != 1:
            return self.ui.print('Only one item can be equipped or unequipped at a time.')

        item_instance: ItemInstance | None = self.command.get_item_instance()

        if not item_instance:
            return self.ui.print(f"Item '{self.command.argument}' is not a valid argument.")

        if not isinstance(item_instance.base, Equippable):
            return self.ui.print(f"Item '{item_instance}' is not equippable.")

        if self.command.subcommand == 'equip':
            result: Result = self.player.equip(item_instance)
        elif self.command.subcommand == 'unequip':
            result: Result = self.player.unequip(item_instance)

        self.ui.print(result.msg)