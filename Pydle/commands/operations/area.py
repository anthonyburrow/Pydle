from ...lib.areas import AREAS
from ...util.structures.Operation import Operation


class AreaOperation(Operation):

    name: str = 'area'
    aliases: list[str] = ['a', 'location', 'loc']
    subcommands: list[str] = ['list']
    help_info: str = "Display the player's current location."

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @classmethod
    def usage(cls) -> str:
        msg: list[str] = []

        msg.append('Use cases:')
        msg.append(f'- area')
        msg.append(f'- area list')
        msg.append(f'- area [area]')

        return '\n'.join(msg)

    def execute(self):
        if not self.command.subcommand and not self.command.argument:
            current_area = AREAS[self.player.area]
            return self.ui.print(f'{self.player} is currently at {current_area}.')

        if self.command.subcommand == 'list':
            msg = []
            msg.append('Available areas:')
            for area in AREAS.values():
                msg.append(f'- {area}')
            return self.ui.print('\n'.join(msg), multiline=True)

        if self.command.argument not in AREAS:
            return self.ui.print(f'{self.command.argument} is not a valid area.')

        self.ui.print(AREAS[self.command.argument].detailed_info(), multiline=True)
