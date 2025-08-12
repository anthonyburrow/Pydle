from ..Operation import Operation
from ...util.player.SkillType import SkillType


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
            skill_type: SkillType = SkillType.from_string(self.command.argument)
            self.ui.print(self.player.get_skill(skill_type).details())
        except ValueError:
            self.ui.print(f'{self.command.argument} is not a valid skill.')
