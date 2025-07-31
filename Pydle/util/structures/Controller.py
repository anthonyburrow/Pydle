import sys
import time
import threading

from .Player import Player
from .UserInterface import UserInterface
from .Activity import Activity, ActivitySetupResult
from ..input import parse_command, flush_input
from ..ticks import Ticks


class Controller:

    def __init__(self, player: Player, ui: UserInterface):
        self.player: Player = player
        self.ui: UserInterface = ui

    def loop(self):
        while True:
            try:
                self.listen()
            except Exception as e:
                self.ui.print_error(e)
                continue

            self.player.save()

    def listen(self):
        flush_input()
        command: str = self.ui.get_command()
        command: dict = parse_command(command)

        command_type = command['type']

        if command_type == 'activity':
            self.control_activity(command)
        elif command_type == 'operation':
            self.control_operation(command)
        elif command_type == 'exit':
            sys.exit()
        elif command_type == 'unknown':
            self.ui.print('Unknown command.')

    def control_activity(self, command: dict):
        activity: Activity = command['activity'](
            self.player, self.ui, *command['args']
        )

        result_setup: ActivitySetupResult = activity.setup()
        if not result_setup.success:
            self.ui.print(result_setup.msg)
            return

        activity.begin()

        tick_duration = Ticks(1)
        while activity.is_active:
            # Still needs work...but step in the right direction
            thread = threading.Thread(target=activity.update)
            thread.start()

            time.sleep(tick_duration)

            thread.join()

        activity.finish()
        time.sleep(Ticks(4))

    def control_operation(self, command: dict):
        function = command['function']
        function(self.player, self.ui, *command['args'])
