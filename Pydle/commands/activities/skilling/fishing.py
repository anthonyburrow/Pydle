from ...Activity import (
    ActivityCheckResult,
    ActivityMsgType,
    ActivityTickResult
)
from ...GatheringActivity import GatheringActivity
from ....lib.areas import AREAS
from ....lib.skilling.fishing import FISH
from ....util.items.ItemInstance import ItemInstance
from ....util.items.ItemRegistry import ITEM_REGISTRY
from ....util.items.skilling.Fish import Fish
from ....util.player.Bank import Bank
from ....util.player.ToolSlot import ToolSlot
from ....util.structures.Area import Area


class FishingActivity(GatheringActivity):

    name: str = 'fish'
    help_info: str = 'Begin fishing for fish.'

    def __init__(self, *args):
        super().__init__(*args)

    @classmethod
    def usage(cls) -> str:
        msg: list[str] = []

        msg.append('Use cases:')
        msg.append('- fish [fish]')

        msg.append('')

        msg.append('Available fish:')
        for item_id in FISH:
            fish: Fish = ITEM_REGISTRY[item_id]
            msg.append(f'- {fish}')

        return '\n'.join(msg)

    @property
    def tool(self) -> ItemInstance | None:
        return self.player.get_tool(ToolSlot.FISHING_ROD)

    def check(self) -> ActivityCheckResult:
        result: ActivityCheckResult = super().check()
        if not result.success:
            return result

        if not isinstance(self.gatherable.base, Fish):
            return ActivityCheckResult(
                success=False,
                msg=f'{self.gatherable} is not a valid fish.'
            )

        if not self._has_level_requirement('fishing', self.gatherable.level):
            return ActivityCheckResult(
                success=False,
                msg=f'You must have Level {self.gatherable.level} Fishing to fish {self.gatherable}.'
            )

        area: Area = AREAS[self.player.area]
        if not area.contains_fish(self.gatherable):
            return ActivityCheckResult(
                success=False,
                msg=f'{area} does not have {self.gatherable} anywhere.'
            )

        if not self.tool:
            return ActivityCheckResult(
                success=False,
                msg=f'{self.player} does not have a fishing rod equipped.'
            )

        return ActivityCheckResult(success=True)

    def begin(self) -> None:
        super().begin()

    def _perform_action(self) -> ActivityTickResult:
        items: Bank = self.loot_table.roll()
        if not items:
            return ActivityTickResult(
                msg=self.standby_text,
                msg_type=ActivityMsgType.WAITING,
            )

        return ActivityTickResult(
            msg=f'Fished {items.list_concise()}!',
            items=items,
            xp={
                'fishing': self.gatherable.xp,
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
        return f'{self.player} is now fishing {self.gatherable}.'

    @property
    def standby_text(self) -> str:
        return 'Fishing...'

    @property
    def finish_text(self) -> str:
        return f'{self.player} finished fishing.'

    def _setup_loot_table(self):
        super()._setup_loot_table()

        fishing_args = {
            'level': self.player.get_level('fishing'),
            'tool': self.tool,
        }
        prob_success = self.gatherable.prob_success(**fishing_args)

        self.gatherable.set_quantity(self.gatherable.n_per_gather)

        self.loot_table = (
            self.loot_table
            .tertiary(self.gatherable, prob_success)
        )

        # Add more stuff (pets, etc)
