from typing import cast

from ....lib.skilling.smithing import SMITHABLES
from ....lib.skilling.woodcutting import LOGS
from ....util.items.ItemInstance import ItemInstance
from ....util.items.ItemParser import ITEM_PARSER
from ....util.items.ItemRegistry import ITEM_REGISTRY
from ....util.items.Quality import Quality
from ....util.items.skilling.Smithable import Smithable
from ....util.player.Bank import Bank
from ....util.player.SkillType import SkillType
from ...Activity import ActivityCheckResult, ActivityTickResult
from ...ProductionActivity import ProductionActivity

fire_effect = 'smithing fire'


class SmithingActivity(ProductionActivity[Smithable]):
    name: str = 'smith'
    help_info: str = 'Begin smithing items.'
    produceable_cls = Smithable

    def __init__(self, *args):
        super().__init__(*args)

    @classmethod
    def usage(cls) -> str:
        msg: list[str] = []

        msg.append('Use cases:')
        msg.append('- smith [item]')

        msg.append('')

        msg.append('Available items:')
        for item_id in SMITHABLES:
            smithable: Smithable = cast(
                Smithable, ITEM_REGISTRY.get(item_id, Smithable)
            )
            msg.append(f'- {smithable}')

        return '\n'.join(msg)

    def check(self) -> ActivityCheckResult:
        result: ActivityCheckResult = super().check()
        if not result.success:
            return result

        if not self._has_level_requirement(
            SkillType.SMITHING, self.produceable.level
        ):
            return ActivityCheckResult(
                success=False,
                msg=f'{self.player} must have Level {self.produceable.level} Smithing to smith a {self.produceable}.',
            )

        if not self.player.has_effect(fire_effect):
            for item_id in LOGS:
                item_instance: ItemInstance = ITEM_PARSER.get_instance_by_id(
                    item_id
                )
                if self.player.has(item_instance):
                    break
            else:
                return ActivityCheckResult(
                    success=False,
                    msg=f'{self.player} has no logs to make a fire.',
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
            msg=f'Smithed a {self.produceable}!',
            items=items,
            xp={
                SkillType.SMITHING: xp,
            },
        )

    def _recheck(self) -> ActivityCheckResult:
        result: ActivityCheckResult = super()._recheck()
        if not result.success:
            return result

        if not self.player.has_effect(fire_effect):
            for item_id in LOGS:
                item_instance: ItemInstance | None = (
                    ITEM_PARSER.get_instance_by_id(item_id)
                )
                if self.player.has(item_instance):
                    self.player.remove(item_instance)
                    self.player.add_effect(
                        fire_effect, item_instance.ticks_per_fire
                    )
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
        return f'{self.player} is now smithing a {self.produceable}.'

    @property
    def standby_text(self) -> str:
        return 'Smithing...'

    @property
    def finish_text(self) -> str:
        return f'{self.player} finished smithing.'

    def _setup_loot_table(self):
        item_kwargs: dict = {
            'item_id': self.produceable.item_id,
            'quantity': self.produceable.n_per_produce,
        }
        self.loot_table = (
            self.loot_table.add(
                ItemInstance(quality=Quality.POOR, **item_kwargs), 1.0
            )
            .add(ItemInstance(quality=Quality.GOOD, **item_kwargs), 1.0)
            .add(ItemInstance(quality=Quality.GREAT, **item_kwargs), 1.0)
            .add(ItemInstance(quality=Quality.SUPERIOR, **item_kwargs), 1.0)
            .add(ItemInstance(quality=Quality.MASTER, **item_kwargs), 1.0)
        )

        # Add more stuff (pets, etc)
