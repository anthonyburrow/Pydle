import sys
import time
import threading

from .Player import Player
from .UserInterface import UserInterface
from .Activity import Activity, ActivitySetupResult
from ..input import flush_input
from ..Command import Command, CommandType
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
        raw_in: str = self.ui.get_input()
        command: Command = Command(raw_in)

        if command.type == CommandType.ACTIVITY:
            self.control_activity(command)
        elif command.type == CommandType.OPERATION:
            self.control_operation(command)
        elif command.type == CommandType.EXIT:
            sys.exit()
        elif command.type == CommandType.UNKNOWN:
            self.ui.print('Unknown command.')

    def control_activity(self, command: Command):
        activity: Activity = command.command_activity(
            self.player, self.ui, command
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

    def control_operation(self, command: Command):
        command.command_function(self.player, self.ui, command)
