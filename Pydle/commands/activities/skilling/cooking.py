from ...Activity import (
    ActivityCheckResult,
    ActivityTickResult
)
from ...ProductionActivity import ProductionActivity
from ....lib.skilling.cooking import COOKABLES
from ....lib.skilling.woodcutting import LOGS
from ....util.items.ItemInstance import ItemInstance
from ....util.items.ItemParser import ITEM_PARSER
from ....util.items.ItemRegistry import ITEM_REGISTRY
from ....util.items.skilling.Cookable import Cookable
from ....util.player.Bank import Bank
from ....util.player.SkillType import SkillType


fire_effect = 'cooking fire'


class CookingActivity(ProductionActivity):

    name: str = 'cook'
    help_info: str = 'Begin cooking food.'

    def __init__(self, *args):
        super().__init__(*args)

    @classmethod
    def usage(cls) -> str:
        msg: list[str] = []

        msg.append('Use cases:')
        msg.append('- cook [food]')

        msg.append('')

        msg.append('Available foods:')
        for item_id in COOKABLES:
            cookable: Cookable = ITEM_REGISTRY[item_id]
            msg.append(f'- {cookable}')

        return '\n'.join(msg)

    def check(self) -> ActivityCheckResult:
        result: ActivityCheckResult = super().check()
        if not result.success:
            return result

        if not isinstance(self.produceable.base, Cookable):
            return ActivityCheckResult(
                success=False,
                msg=f'{self.produceable} is not a valid cookable item.'
            )

        if not self._has_level_requirement(SkillType.COOKING, self.produceable.level):
            return ActivityCheckResult(
                success=False,
                msg=f'{self.player} must have Level {self.produceable.level} Cooking to cook {self.produceable}.'
            )

        if not self.player.has_effect(fire_effect):
            for item_id in LOGS:
                item_instance: ItemInstance | None = \
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

        if not items:
            return ActivityTickResult(
                msg=f'Burned {self.produceable}...',
                xp={
                    SkillType.COOKING: xp * 0.5,
                },
            )

        return ActivityTickResult(
            msg=f'Cooked {self.produceable}!',
            items=items,
            xp={
                SkillType.COOKING: xp,
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
        return f'{self.player} is now cooking {self.produceable}.'

    @property
    def standby_text(self) -> str:
        return 'Cooking...'

    @property
    def finish_text(self) -> str:
        return f'{self.player} finished cooking.'

    def _setup_loot_table(self):
        super()._setup_loot_table()

        cooking_args = {
            'level': self.player.get_level(SkillType.COOKING),
        }
        prob_success = self.produceable.prob_success(**cooking_args)

        self.loot_table = (
            self.loot_table
            .tertiary(self.produceable, prob_success)
        )

        # Add more stuff (pets, etc)
