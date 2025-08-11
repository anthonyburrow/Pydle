from ...Activity import (
    ActivityCheckResult,
    ActivityTickResult
)
from ...ProductionActivity import ProductionActivity
from ....lib.skilling.smithing import SMELTABLES
from ....lib.skilling.woodcutting import LOGS
from ....util.items.ItemInstance import ItemInstance
from ....util.items.ItemParser import ITEM_PARSER
from ....util.items.ItemRegistry import ITEM_REGISTRY
from ....util.items.skilling.Smeltable import Smeltable
from ....util.player.Bank import Bank


fire_effect = 'smithing fire'


class SmeltingActivity(ProductionActivity):

    name: str = 'smelt'
    help_info: str = 'Begin smelting ores into bars.'

    def __init__(self, *args):
        super().__init__(*args)

    @classmethod
    def usage(cls) -> str:
        msg: list[str] = []

        msg.append('Use cases:')
        msg.append('- smelt [ore]')

        msg.append('')

        msg.append('Available ores:')
        for item_id in SMELTABLES:
            smeltable: Smeltable = ITEM_REGISTRY[item_id]
            msg.append(f'- {smeltable}')

        return '\n'.join(msg)

    def check(self) -> ActivityCheckResult:
        result: ActivityCheckResult = super().check()
        if not result.success:
            return result

        if not isinstance(self.produceable.base, Smeltable):
            return ActivityCheckResult(
                success=False,
                msg=f'{self.produceable} is not a valid smeltable item.'
            )

        if not self._has_level_requirement('smithing', self.produceable.level):
            return ActivityCheckResult(
                success=False,
                msg=f'{self.player} must have Level {self.produceable.level} Smithing to smelt a {self.produceable}.'
            )

        if not self.player.has_effect(fire_effect):
            for item_id in LOGS:
                item_instance: ItemInstance = \
                    ITEM_PARSER.get_instance_by_id(item_id)
                if self.player.has(item_instance):
                    break
            else:
                return ActivityCheckResult(
                    success=False,
                    msg=f'{self.player} has no logs to make a fire.'
                )

        return ActivityCheckResult(success=True)

    def begin(self) -> None:
        super().begin()

    def _perform_action(self) -> ActivityTickResult:
        for item_instance in self.items_required:
            self.player.remove(item_instance)

        items: Bank = self.loot_table.roll()
        xp: float = self.produceable.xp if self.produceable else 0.

        return ActivityTickResult(
            msg=f'Smelted a {self.produceable}!',
            items=items,
            xp={
                'smithing': xp,
            },
        )

    def _recheck(self) -> ActivityCheckResult:
        result: ActivityCheckResult = super()._recheck()
        if not result.success:
            return result

        if not self.player.has_effect(fire_effect):
            for item_id in LOGS:
                item_instance: ItemInstance | None = \
                    ITEM_PARSER.get_instance_by_id(item_id)
                if self.player.has(item_instance):
                    self.player.remove(item_instance)
                    self.player.add_effect(fire_effect, item_instance.ticks_per_fire)
                    break
            else:
                return ActivityCheckResult(
                    msg=f'{self.player} ran out of logs.',
                    success=False,
                )

        return ActivityCheckResult(success=True)

    def finish(self) -> None:
        super().finish()

    @property
    def startup_text(self) -> str:
        return f'{self.player} is now smelting a {self.produceable}.'

    @property
    def standby_text(self) -> str:
        return 'Smelting...'

    @property
    def finish_text(self) -> str:
        return f'{self.player} finished smelting.'

    def _setup_loot_table(self):
        self.loot_table = (
            self.loot_table
            .every(self.produceable)
        )

        # Add more stuff (pets, etc)
