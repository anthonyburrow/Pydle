from abc import ABC, abstractmethod

from .Activity import (
    Activity,
    ActivityMsgType,
    ActivitySetupResult,
    ActivityTickResult,
)
from .CommandRegistry import COMMAND_REGISTRY
from .CommandType import CommandType
from ..util.items.ItemInstance import ItemInstance
from ..util.structures.LootTable import LootTable


class GatheringActivity(Activity, ABC):

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)

        COMMAND_REGISTRY.register(cls, CommandType.ACTIVITY)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.gatherable: ItemInstance | None = self.command.get_item_instance()
        self.loot_table: LootTable = LootTable()

    @property
    @abstractmethod
    def tool(self) -> ItemInstance | None:
        pass

    def setup(self) -> ActivitySetupResult:
        result: ActivitySetupResult = super().setup()
        if not result.success:
            return result

        if self.gatherable is None:
            return ActivitySetupResult(
                success=False,
                msg='A valid item was not given.'
            )

        return ActivitySetupResult(success=True)

    def begin(self) -> None:
        self._setup_loot_table()

        super().begin()

    def _process_tick(self) -> ActivityTickResult:
        ticks_per_use = self.tool.ticks_per_use
        if self.tick_count % ticks_per_use:
            return ActivityTickResult(
                msg=self.standby_text,
                msg_type=ActivityMsgType.WAITING,
            )

        return self._perform_action()

    @abstractmethod
    def _perform_action(self) -> ActivityTickResult:
        pass

    def _recheck(self) -> ActivitySetupResult:
        result: ActivitySetupResult = super()._recheck()
        if not result.success:
            return result

        return ActivitySetupResult(success=True)

    def finish(self) -> None:
        super().finish()

    def _on_levelup(self) -> None:
        super()._on_levelup()

        self._setup_loot_table()

    def _setup_loot_table(self) -> None:
        pass
