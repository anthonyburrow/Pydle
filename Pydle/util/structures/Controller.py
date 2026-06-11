import threading
import time
from typing import cast

from .UserInterface import UserInterface
from ..ticks import Ticks
from ..player.Player import Player
from ...commands.Activity import Activity, ActivityCheckResult
from ...commands.Command import Command, EmptyCommandError, InvalidCommandError
from ...commands.CommandType import CommandType
from ...commands.Operation import Operation


class Controller:

    def __init__(self, player: Player, ui: UserInterface):
        self.player: Player = player
        self.ui: UserInterface = ui

    def loop(self):
        while True:
            try:
                self.listen()
            except Exception as e:
                self.ui.print_exception(e)
                continue

            self.player.save()

    def listen(self):
        self.ui.flush_input()

        raw_in: str = self.ui.get_input()
        try:
            command: Command = Command.parse(raw_in)
        except EmptyCommandError:
            return
        except InvalidCommandError:
            self.ui.print('Unknown command.')
            return

        if command.type == CommandType.ACTIVITY:
            self.control_activity(command)
        elif command.type == CommandType.OPERATION:
            self.control_operation(command)

    def control_activity(self, command: Command):
        activity_cls: type[Activity] = cast(type[Activity], command.action)
        activity: Activity = activity_cls(
            self.player, self.ui, command
        )

        result_check: ActivityCheckResult = activity.check()
        if not result_check.success:
            self.ui.print(result_check.msg)
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
        operation_cls: type[Operation] = cast(type[Operation], command.action)
        operation: Operation = operation_cls(
            self.player, self.ui, command
        )
        operation.execute()
