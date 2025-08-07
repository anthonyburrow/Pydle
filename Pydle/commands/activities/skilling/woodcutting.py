from ....lib.areas import AREAS
from ....lib.skilling.woodcutting import LOGS
from ....util.items.ItemInstance import ItemInstance
from ....util.items.ItemParser import ITEM_PARSER
from ....util.items.ItemRegistry import ITEM_REGISTRY
from ....util.items.skilling.Log import Log
from ....util.player.Bank import Bank
from ....util.player.ToolSlot import ToolSlot
from ....util.structures.Activity import (
    Activity,
    ActivitySetupResult,
    ActivityMsgType,
    ActivityTickResult
)
from ....util.structures.Area import Area
from ....util.structures.LootTable import LootTable


class WoodcuttingActivity(Activity):

    def __init__(self, *args):
        super().__init__(*args)

        self.log: ItemInstance | None = self.command.get_item_instance()
        self.log.set_quantity(self.log.n_per_gather)

        self.axe: ItemInstance = self.player.get_tool(ToolSlot.AXE)
        self.loot_table: LootTable = None

        self.description: str = 'woodcutting'

    def setup_inherited(self) -> ActivitySetupResult:
        if self.log is None:
            return ActivitySetupResult(
                success=False,
                msg='A valid log was not given.'
            )

        if not isinstance(self.log.base, Log):
            return ActivitySetupResult(
                success=False,
                msg=f'{self.log} is not a valid log.'
            )

        skill_level: int = self.player.get_level('woodcutting')
        if skill_level < self.log.level:
            return ActivitySetupResult(
                success=False,
                msg=f'You must have Level {self.log.level} Woodcutting to chop {self.log}.'
            )

        area: Area = AREAS[self.player.area]
        if not area.contains_log(self.log):
            return ActivitySetupResult(
                success=False,
                msg=f'{area} does not have {self.log} anywhere.'
            )

        if not self.axe:
            return ActivitySetupResult(
                success=False,
                msg=f'{self.player} does not have an axe.'
            )

        self._setup_loot_table()

        return ActivitySetupResult(success=True)

    def update_inherited(self) -> ActivityTickResult:
        '''Processing during each tick.'''
        ticks_per_use = self.axe.ticks_per_use
        if self.tick_count % ticks_per_use:
            return ActivityTickResult(
                msg=self.standby_text,
                msg_type=ActivityMsgType.WAITING,
            )

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
                'woodcutting': self.log.xp,
            },
        )

    def finish_inherited(self):
        pass

    def reset_on_levelup(self):
        self._setup_loot_table()

    @property
    def startup_text(self) -> str:
        return f'{self.player} is now chopping {self.log}.'

    @property
    def standby_text(self) -> str:
        return 'Chopping...'

    @property
    def finish_text(self) -> str:
        return f'{self.player} finished {self.description}.'

    def _setup_loot_table(self):
        woodcutting_args = {
            'level': self.player.get_level('woodcutting'),
            'tool': self.axe,
        }
        prob_success = self.log.prob_success(**woodcutting_args)

        self.loot_table = (
            LootTable()
            .tertiary(self.log, prob_success)
        )

        # Add more stuff (pets, etc)


def detailed_info():
    msg: list = []

    msg.append('Use cases:')
    msg.append('- chop [log]')

    msg.append('')

    msg.append('Available logs:')
    for item_id in LOGS:
        log: Log = ITEM_REGISTRY[item_id]
        msg.append(f'- {log}')

    return '\n'.join(msg)
