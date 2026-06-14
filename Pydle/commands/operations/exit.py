import sys

from ..Operation import Operation


class ExitOperation(Operation):
    name: str = 'exit'
    aliases: list[str] = ['quit']
    subcommands: list[str] = []
    help_info: str = 'Exit the game.'

    @classmethod
    def usage(cls) -> str:
        return 'Use cases:\n- exit'

    def execute(self) -> None:
        sys.exit()
