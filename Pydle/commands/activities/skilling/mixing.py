from typing import cast

from ....lib.skilling.herblore import MIXABLES
from ....util.items.ItemInstance import ItemInstance
from ....util.items.ItemRegistry import ITEM_REGISTRY
from ....util.items.skilling.Mixable import Mixable
from ....util.player.Bank import Bank
from ....util.player.SkillType import SkillType
from ...Activity import ActivityCheckResult, ActivityTickResult
from ...ProductionActivity import ProductionActivity


class MixingActivity(ProductionActivity[Mixable]):
    name: str = 'mix'
    help_info: str = 'Begin mixing potions.'
    produceable_cls = Mixable

    def __init__(self, *args):
        super().__init__(*args)

    @classmethod
    def usage(cls) -> str:
        msg: list[str] = []

        msg.append('Use cases:')
        msg.append('- mix [potion]')

        msg.append('')

        msg.append('Available potions:')
        for item_id in MIXABLES:
            mixable: Mixable = cast(
                Mixable, ITEM_REGISTRY.get(item_id, Mixable)
            )
            msg.append(f'- {mixable}')

        return '\n'.join(msg)

    def check(self) -> ActivityCheckResult:
        result: ActivityCheckResult = super().check()
        if not result.success:
            return result

        if not self._has_level_requirement(
            SkillType.HERBLORE, self.produceable.level
        ):
            return ActivityCheckResult(
                success=False,
                msg=f'{self.player} must have Level {self.produceable.level} Herblore to mix a {self.produceable}.',
            )

        return ActivityCheckResult(success=True)

    def begin(self) -> None:
        super().begin()

    def _perform_action(self) -> ActivityTickResult:
        for item_instance in self.items_required:
            self.player.remove(item_instance)

        items: Bank = self.loot_table.roll()
        xp: float = self.produceable.xp if self.produceable else 0.0

        return ActivityTickResult(
            msg=f'Mixed a {self.produceable}!',
            items=items,
            xp={
                SkillType.HERBLORE: xp,
            },
        )

    def _recheck(self) -> ActivityCheckResult:
        result: ActivityCheckResult = super()._recheck()
        if not result.success:
            return result

        return ActivityCheckResult(success=True)

    def finish(self) -> None:
        super().finish()

    @property
    def startup_text(self) -> str:
        return f'{self.player} is now mixing a {self.produceable}.'

    @property
    def standby_text(self) -> str:
        return 'Mixing...'

    @property
    def finish_text(self) -> str:
        return f'{self.player} finished mixing.'

    def _setup_loot_table(self):
        super()._setup_loot_table()

        produced: ItemInstance = ItemInstance(
            item_id=self.produceable.item_id,
            quantity=self.produceable.n_per_produce,
        )

        self.loot_table = self.loot_table.every(produced)

        # % chance for number of doses

        # Add more stuff (pets, etc)
