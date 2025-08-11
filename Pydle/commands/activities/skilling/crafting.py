from ...Activity import (
    ActivitySetupResult,
    ActivityTickResult
)
from ...ProductionActivity import ProductionActivity
from ....lib.skilling.crafting import CRAFTABLES
from ....util.items.ItemRegistry import ITEM_REGISTRY
from ....util.items.skilling.Craftable import Craftable
from ....util.player.Bank import Bank


class CraftingActivity(ProductionActivity):

    name: str = 'craft'
    help_info: str = 'Begin crafting an item.'

    def __init__(self, *args):
        super().__init__(*args)

    @classmethod
    def usage(cls) -> str:
        msg: list[str] = []

        msg.append('Use cases:')
        msg.append('- craft [item]')

        msg.append('')

        msg.append('Available items:')
        for item_id in CRAFTABLES:
            craftable: Craftable = ITEM_REGISTRY[item_id]
            msg.append(f'- {craftable}')

        return '\n'.join(msg)

    def setup(self) -> ActivitySetupResult:
        result: ActivitySetupResult = super().setup()
        if not result.success:
            return result

        if not isinstance(self.produceable.base, Craftable):
            return ActivitySetupResult(
                success=False,
                msg=f'{self.produceable} is not a valid craftable item.'
            )

        if not self._has_level_requirement('crafting', self.produceable.level):
            return ActivitySetupResult(
                success=False,
                msg=f'{self.player} must have Level {self.produceable.level} Crafting to craft a {self.produceable}.'
            )

        return ActivitySetupResult(success=True)

    def begin(self) -> None:
        super().begin()

    def _perform_action(self) -> ActivityTickResult:
        for item_instance in self.items_required:
            self.player.remove(item_instance)

        items: Bank = self.loot_table.roll()
        xp: float = self.produceable.xp if self.produceable else 0.

        return ActivityTickResult(
            msg=f'Crafted a {self.produceable}!',
            items=items,
            xp={
                'crafting': xp,
            },
        )

    def _recheck(self) -> ActivitySetupResult:
        result: ActivitySetupResult = super()._recheck()
        if not result.success:
            return result

        return ActivitySetupResult(success=True)

    def finish(self) -> None:
        super().finish()

    @property
    def startup_text(self) -> str:
        return f'{self.player} is now crafting a {self.produceable}.'

    @property
    def standby_text(self) -> str:
        return 'Crafting...'

    @property
    def finish_text(self) -> str:
        return f'{self.player} finished crafting.'

    def _setup_loot_table(self):
        super()._setup_loot_table()

        self.loot_table = (
            self.loot_table
            .every(self.produceable)
        )

        # Add more stuff (pets, etc)
