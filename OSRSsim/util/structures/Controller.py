import sys

from . import Player, Activity
from ..output import print_output
from ..input import parse_command, flush_input
from ..misc import get_client_ID


class Controller:

    def __init__(self, player: Player):
        self.player: Player = player
        self.client_ID = get_client_ID()

    def loop(self):
        while True:
            self.listen()
            self.player.save()

    def listen(self):
        flush_input()
        command: str = input('> ')
        command: dict = parse_command(command)

        if command['type'] == 'activity':
            self.control_activity(command)
        elif command['type'] == 'info':
            self.control_info(command)
        elif command['type'] == 'testing':
            self.control_testing(command)
        elif command['type'] == 'exit':
            sys.exit()
        else:
            print('Unknown command.')

    def control_activity(self, command: dict):
        _activity: Activity = command['activity']
        _activity_args: tuple = command['args']

        activity = _activity(self, *_activity_args)

        setup = activity.setup()
        if not setup['success']:
            print_output(setup['status_msg'])
            return

        activity.begin_loop()

    def control_info(self, command: dict):
        func = command['function']
        func(self.player, *command['args'])

    def control_testing(self, command: dict):
        func = command['function']
        func(self.player)
