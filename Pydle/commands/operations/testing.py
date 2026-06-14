from ..Operation import Operation
from ..testing.setups import SETUP_MANAGER
from ...util.player.SkillType import SkillType


class TestingOperation(Operation):

    name: str = 'testing'
    aliases: list[str] = ['test']
    subcommands: list[str] = ['setup', 'set_level']
    help_info: str = 'Non-production testing commands.'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @classmethod
    def usage(cls) -> str:
        msg: list[str] = []

        msg.append('Use cases:')
        msg.append('- testing setup [name]')
        msg.append('- testing set_level [skill] [level]')
        msg.append('')
        msg.append('Available setups:')
        for setup_name in SETUP_MANAGER.names():
            msg.append(f'- {setup_name}')

        return '\n'.join(msg)

    def execute(self):
        if not self.command.subcommand:
            return self.ui.print('A subcommand for `testing` is needed.')

        if self.command.subcommand == 'setup':
            if not self.command.argument:
                msg: str = 'A setup name is needed. Use `testing setup [name]`.'
                return self.ui.print(msg)

            if not SETUP_MANAGER.has_setup(self.command.argument):
                setup_names: str = ', '.join(SETUP_MANAGER.names())
                return self.ui.print(
                    f'Unknown setup `{self.command.argument}`. Available: {setup_names}'
                )

            SETUP_MANAGER.apply(self.player, self.command.argument)

            return self.ui.print(f'Applied testing setup `{self.command.argument}`.')

        if self.command.subcommand == 'set_level':
            args: list[str] = self.command.argument.split()
            if len(args) != 2:
                return self.ui.print('Usage: `testing set_level [skill] [level]`.')

            skill_name, level_str = args

            try:
                skill_type: SkillType = SkillType.from_string(skill_name)
            except ValueError:
                return self.ui.print(f'Invalid skill `{skill_name}`.')

            try:
                level: int = int(level_str)
            except ValueError:
                return self.ui.print(f'Invalid level `{level_str}`.')

            try:
                self.player.set_level(skill_type, level)
            except KeyError:
                return self.ui.print(f'Invalid level `{level}`.')

            return self.ui.print(f'Set {skill_type} to level {level}.')

        self.ui.print(f'Unknown subcommand `{self.command.subcommand}`')
