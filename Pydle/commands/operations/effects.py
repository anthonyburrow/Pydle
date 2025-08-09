from ..Operation import Operation


class EffectsOperation(Operation):

    name: str = 'effects'
    aliases: list[str] = ['effect']
    subcommands: list[str] = []
    help_info: str = "Display and equip the player's ongoing effects."

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @classmethod
    def usage(cls) -> str:
        msg: list[str] = []

        msg.append('Use cases:')
        msg.append('- effects')

        return '\n'.join(msg)

    def execute(self):
        if not self.command.subcommand and not self.command.argument:
            return self.ui.print(str(self.player.updated_effects), multiline=True)