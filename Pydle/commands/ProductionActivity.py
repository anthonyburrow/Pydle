from abc import ABC, abstractmethod
from typing import Generic, TypeVar, cast

from .Activity import (
    Activity,
    ActivityMsgType,
    ActivityCheckResult,
    ActivityTickResult,
)
from .CommandRegistry import COMMAND_REGISTRY
from .CommandType import CommandType
from ..util.items.Item import Item
from ..util.items.ItemInstance import ItemInstance
from ..util.items.ItemParser import ITEM_PARSER
from ..util.items.Produceable import Produceable
from ..util.structures.LootTable import LootTable


T_Produceable = TypeVar('T_Produceable', bound=Produceable)


class ProductionActivity(Activity, Generic[T_Produceable], ABC):
    produceable_cls: type[T_Produceable]

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)

        COMMAND_REGISTRY.register(cls, CommandType.ACTIVITY)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._produceable: T_Produceable | None = None
        self.items_required: list[ItemInstance] = []
        self.loot_table: LootTable = LootTable()

    @property
    def produceable(self) -> T_Produceable:
        if self._produceable is None:
            raise RuntimeError('produceable is not initialized; call check() before begin().')

        return self._produceable

    def check(self) -> ActivityCheckResult:
        result: ActivityCheckResult = super().check()
        if not result.success:
            return result

        if not self.command.has_valid_item_argument():
            return ActivityCheckResult(
                success=False,
                msg='A valid item was not given.'
            )

        base_item: Item = self.command.get_item_base()
        expected_type: type[T_Produceable] = self.produceable_cls
        if not isinstance(base_item, expected_type):
            return ActivityCheckResult(
                success=False,
                msg=f'{base_item} is not a valid {expected_type.__name__.lower()} item.'
            )

        self._produceable = cast(T_Produceable, base_item)

        self.items_required = []
        for item_name, quantity in self.produceable.items_required.items():
            self.items_required.append(
                ITEM_PARSER.get_instance(item_name, quantity)
            )

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
        ticks_per_action = self.produceable.ticks_per_action
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
