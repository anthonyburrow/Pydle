from ...util.structures.Operation import Operation


class BankOperation(Operation):

    name: str = 'bank'
    aliases: list[str] = ['b']
    subcommands: list[str] = []
    help_info: str = "Display the player's bank."

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @classmethod
    def usage(cls) -> str:
        msg: list[str] = []

        msg.append('Use cases:')
        msg.append('- bank')

        return '\n'.join(msg)

    def execute(self):
        if not self.command.subcommand and not self.command.argument:
            return self.ui.print(str(self.player.bank), multiline=True)