import sys
import time
import threading
from colorama import just_fix_windows_console

from . import Player
from .Activity import Activity, ActivitySetupResult
from ..output import print_info, print_error
from ..input import parse_command, flush_input
from ..commands import COMMAND_PREFIX
from ..misc import get_client_ID
from ..ticks import Ticks


class Controller:

    def __init__(self, player: Player):
        self.player: Player = player
        self.client_ID: int = get_client_ID()

        # Allow Colorama/termcolor to work on Windows (does nothing if Unix/Mac)
        just_fix_windows_console()

    def loop(self):
        while True:
            try:
                self.listen()
            except Exception as e:
                print_error(e)
                continue

            self.player.save()

    def listen(self):
        flush_input()
        command: str = input(COMMAND_PREFIX)
        command: dict = parse_command(command)

        command_type = command['type']

        if command_type == 'activity':
            self.control_activity(command)
        elif command_type == 'operation':
            self.control_operation(command)
        elif command_type == 'exit':
            sys.exit()
        elif command_type == 'unknown':
            print_info('Unknown command.')

    def control_activity(self, command: dict):
        activity: Activity = command['activity'](
            self.player, self.client_ID, *command['args']
        )

        result_setup: ActivitySetupResult = activity.setup()
        if not result_setup.success:
            print_info(result_setup.msg)
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
        function(self.player, *command['args'])
