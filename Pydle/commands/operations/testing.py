from ..Operation import Operation
from ..testing.skilling import testing_skilling


class TestingOperation(Operation):

    name: str = 'testing'
    aliases: list[str] = ['test']
    subcommands: list[str] = ['skilling']
    help_info: str = 'Non-production testing commands.'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @classmethod
    def usage(cls) -> str:
        msg: list[str] = []

        msg.append('Use cases:')
        msg.append('- testing skilling')

        return '\n'.join(msg)

    def execute(self):
        if not self.command.subcommand and not self.command.argument:
            return self.ui.print('A subcommand for `testing` is needed.')

        if self.command.subcommand == 'skilling':
            testing_skilling(self.player)
        else:
            self.ui.print(f'Unknown subcommand `{self.command.subcommand}`')
