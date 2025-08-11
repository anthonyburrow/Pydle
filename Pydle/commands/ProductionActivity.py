from abc import ABC, abstractmethod

from .Activity import (
    Activity,
    ActivityMsgType,
    ActivityCheckResult,
    ActivityTickResult,
)
from .CommandRegistry import COMMAND_REGISTRY
from .CommandType import CommandType
from ..util.items.ItemInstance import ItemInstance
from ..util.items.ItemParser import ITEM_PARSER
from ..util.structures.LootTable import LootTable


class ProductionActivity(Activity, ABC):

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)

        COMMAND_REGISTRY.register(cls, CommandType.ACTIVITY)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.produceable: ItemInstance | None = self.command.get_item_instance()
        self.items_required: list[ItemInstance] = []
        self.loot_table: LootTable = LootTable()

    def check(self) -> ActivityCheckResult:
        result: ActivityCheckResult = super().check()
        if not result.success:
            return result

        if self.produceable is None:
            return ActivityCheckResult(
                success=False,
                msg='A valid item was not given.'
            )

        self._setup_items_required()
        for item_instance in self.items_required:
            if self.player.has(item_instance):
                continue
            return ActivityCheckResult(
                success=False,
                msg=f'{self.player} does not have {item_instance.quantity}x {item_instance}.'
            )

        return ActivityCheckResult(success=True)

    def begin(self) -> None:
        self._setup_loot_table()

        super().begin()

    def _process_tick(self) -> ActivityTickResult:
        ticks_per_action = self.produceable.ticks_per_action if self.produceable else 1
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

        for item_instance in self.items_required:
            if self.player.has(item_instance):
                continue
            return ActivityCheckResult(
                msg=f'{self.player} ran out of {item_instance}.',
                success=False,
            )

        return ActivityCheckResult(success=True)

    def finish(self) -> None:
        super().finish()

    def _on_levelup(self) -> None:
        super()._on_levelup()

        self._setup_loot_table()

    def _setup_loot_table(self) -> None:
        pass

    def _setup_items_required(self) -> None:
        if not (self.produceable and self.produceable.items_required):
            return

        for item_name, quantity in self.produceable.items_required.items():
            item_instance: ItemInstance | None = ITEM_PARSER.get_instance(item_name, quantity)
            if not item_instance:
                raise ValueError(f'Invalid item {item_name} in items_required for {self.produceable}.')
            self.items_required.append(item_instance)
