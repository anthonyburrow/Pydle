from ..Operation import Operation


class SkillsOperation(Operation):

    name: str = 'skills'
    aliases: list[str] = ['s', 'skill']
    subcommands: list[str] = []
    help_info: str = "Display the player's skills."

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @classmethod
    def usage(cls) -> str:
        msg: list[str] = []

        msg.append('Use cases:')
        msg.append('- skills')
        msg.append('- skills [skill]')

        return '\n'.join(msg)

    def execute(self):
        if not self.command.subcommand and not self.command.argument:
            return self.ui.print(str(self.player.skills), multiline=True)

        try:
            self.ui.print(self.player.get_skill(self.command.argument).details())
        except KeyError:
            self.ui.print(f'{self.command.argument} is not a valid skill.')
