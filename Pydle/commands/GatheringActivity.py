from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from .Activity import (
    Activity,
    ActivityMsgType,
    ActivityCheckResult,
    ActivityTickResult,
)
from .CommandRegistry import COMMAND_REGISTRY
from .CommandType import CommandType
from ..util.items.ItemInstance import ItemInstance
from ..util.items.Gatherable import Gatherable
from ..util.structures.LootTable import LootTable
from ..util.player.ToolSlot import ToolSlot


T_Gatherable = TypeVar('T_Gatherable', bound=Gatherable)


class GatheringActivity(Activity, Generic[T_Gatherable], ABC):
    gatherable_cls: type[T_Gatherable]
    tool_slot: ToolSlot
    tool_description: str

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)

        COMMAND_REGISTRY.register(cls, CommandType.ACTIVITY)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._gatherable: ItemInstance | None = None
        self._tool: ItemInstance | None = None
        self.loot_table: LootTable = LootTable()

    @property
    def gatherable(self) -> ItemInstance:
        if self._gatherable is None:
            raise RuntimeError('gatherable is not initialized; call check() before begin().')

        return self._gatherable

    @property
    def tool(self) -> ItemInstance:
        if self._tool is None:
            raise RuntimeError('tool is not initialized; call check() before begin().')

        return self._tool

    def check(self) -> ActivityCheckResult:
        result: ActivityCheckResult = super().check()
        if not result.success:
            return result

        if not self.command.has_valid_item_argument():
            return ActivityCheckResult(
                success=False,
                msg='A valid item was not given.'
            )

        gatherable: ItemInstance = self.command.get_item_instance()
        expected_type: type[T_Gatherable] = self.gatherable_cls
        if not isinstance(gatherable.base, expected_type):
            return ActivityCheckResult(
                success=False,
                msg=f'{gatherable} is not a valid {expected_type.__name__.lower()}.'
            )

        self._gatherable = gatherable

        tool: ItemInstance | None = self.player.get_tool(self.tool_slot)
        if not tool:
            return ActivityCheckResult(
                success=False,
                msg=f'{self.player} does not have {self.tool_description} equipped.'
            )

        self._tool = tool

        return ActivityCheckResult(success=True)

    def begin(self) -> None:
        self._setup_loot_table()

        super().begin()

    def _process_tick(self) -> ActivityTickResult:
        ticks_per_action = self.tool.ticks_per_action
        if self.tick_count % ticks_per_action:
            return ActivityTickResult(
                msg=self.standby_text,
                msg_type=ActivityMsgType.WAITING,
            )

        return self._perform_action()

    @abstractmethod
    def _perform_action(self) -> ActivityTickResult:
        pass

    def _recheck(self) -> ActivityCheckResult:
        result: ActivityCheckResult = super()._recheck()
        if not result.success:
            return result

        return ActivityCheckResult(success=True)

    def finish(self) -> None:
        super().finish()

    def _on_levelup(self) -> None:
        super()._on_levelup()

        self._setup_loot_table()

    def _setup_loot_table(self) -> None:
        pass
