from typing import cast

from ....lib.areas import AREAS
from ....lib.skilling.woodcutting import LOGS
from ....util.items.ItemInstance import ItemInstance
from ....util.items.ItemRegistry import ITEM_REGISTRY
from ....util.items.skilling.Log import Log
from ....util.player.Bank import Bank
from ....util.player.SkillType import SkillType
from ....util.player.ToolSlot import ToolSlot
from ....util.structures.Area import Area
from ...Activity import (
    ActivityCheckResult,
    ActivityMsgType,
    ActivityTickResult,
)
from ...GatheringActivity import GatheringActivity


class WoodcuttingActivity(GatheringActivity):
    name: str = 'chop'
    help_info: str = 'Begin chopping wood.'
    gatherable_cls = Log
    tool_slot = ToolSlot.AXE
    tool_description = 'an axe'

    def __init__(self, *args):
        super().__init__(*args)

    @classmethod
    def usage(cls) -> str:
        msg: list[str] = []

        msg.append('Use cases:')
        msg.append('- chop [log]')

        msg.append('')

        msg.append('Available logs:')
        for item_id in LOGS:
            log: Log = cast(Log, ITEM_REGISTRY.get(item_id, Log))
            msg.append(f'- {log}')

        return '\n'.join(msg)

    def check(self) -> ActivityCheckResult:
        result: ActivityCheckResult = super().check()
        if not result.success:
            return result

        if not self._has_level_requirement(
            SkillType.WOODCUTTING, self.gatherable.level
        ):
            return ActivityCheckResult(
                success=False,
                msg=f'You must have Level {self.gatherable.level} Woodcutting to chop {self.gatherable}.',
            )

        area: Area = AREAS[self.player.area]
        if not area.contains_log(self.gatherable):
            return ActivityCheckResult(
                success=False,
                msg=f'{area} does not have {self.gatherable} anywhere.',
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
            msg=f'Chopped {items.list_concise()}!',
            items=items,
            xp={
                'woodcutting': self.gatherable.xp,
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
        return f'{self.player} is now chopping {self.gatherable}.'

    @property
    def standby_text(self) -> str:
        return 'Chopping...'

    @property
    def finish_text(self) -> str:
        return f'{self.player} finished chopping.'

    def _setup_loot_table(self):
        woodcutting_args = {
            'level': self.player.get_level(SkillType.WOODCUTTING),
            'tool': self.tool,
        }
        prob_success = self.gatherable.prob_success(**woodcutting_args)

        self.gatherable.set_quantity(self.gatherable.n_per_gather)

        self.loot_table = self.loot_table.tertiary(
            self.gatherable, prob_success
        )

        # Add more stuff (pets, etc)
