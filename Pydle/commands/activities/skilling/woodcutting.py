from ....util.structures.Activity import (
    Activity,
    ActivitySetupResult,
    ActivityMsgType,
    ActivityTickResult
)
from ....util.structures.LootTable import LootTable
from ....util.structures.Bank import Bank
from ....util.structures.Tool import Tool
from ....lib.skilling.woodcutting import Log, logs


class WoodcuttingActivity(Activity):

    def __init__(self, *args):
        super().__init__(*args)

        if self.argument in logs:
            self.log: Log = logs[self.argument]
        else:
            self.log: Log = None

        self.description: str = 'woodcutting'

        self.axe: Tool = self.player.get_tool('axe')
        self.loot_table: LootTable = None

    def setup_inherited(self) -> ActivitySetupResult:
        if self.log is None:
            return ActivitySetupResult(
                success=False,
                msg='A valid log was not given.'
            )

        skill_level: int = self.player.get_level('woodcutting')
        if skill_level < self.log.level:
            return ActivitySetupResult(
                success=False,
                msg=f'You must have Level {self.log.level} Woodcutting to chop {self.log}.'
            )

        if self.axe is None:
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

        self.loot_table = LootTable()
        self.loot_table.tertiary(
            self.log.name, prob_success, self.log.n_per_gather
        )

        # Add more stuff (pets, etc)


def detailed_info():
    msg: list = []

    msg.append('Use cases:')
    msg.append('- chop [log]')

    msg.append('')

    msg.append('Available logs:')
    for log in logs:
        name = str(log).capitalize()
        msg.append(f'- {name}')

    return '\n'.join(msg)
