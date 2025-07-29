from ....util.structures.Activity import (
    Activity,
    ActivitySetupResult,
    ActivityMsgType,
    ActivityTickResult
)
from ....util.structures.LootTable import LootTable
from ....util.structures.Bank import Bank
from ....util.structures.Tool import Tool
from ....util.structures.Area import Area
from ....lib.skilling.foraging import Herb, HERBS
from ....lib.areas import AREAS


class ForagingActivity(Activity):

    def __init__(self, *args):
        super().__init__(*args)

        if self.argument in HERBS:
            self.herb: Herb = HERBS[self.argument]
            self.herb_key: str = self.argument
        else:
            self.herb: Herb = None

        self.description: str = 'foraging'

        self.secateurs: Tool = self.player.get_tool('secateurs')
        self.loot_table: LootTable = None

    def setup_inherited(self) -> ActivitySetupResult:
        if self.herb is None:
            return ActivitySetupResult(
                success=False,
                msg='A valid herb was not given.'
            )

        skill_level: int = self.player.get_level('foraging')
        if skill_level < self.herb.level:
            return ActivitySetupResult(
                success=False,
                msg=f'You must have Level {self.herb.level} Foraging to collect {self.herb}.'
            )

        area: Area = AREAS[self.player.area]
        if not area.contains_herb(self.herb_key):
            return ActivitySetupResult(
                success=False,
                msg=f'{area} does not have {self.herb} anywhere.'
            )

        if not self.secateurs:
            return ActivitySetupResult(
                success=False,
                msg=f'{self.player} does not have any secateurs.'
            )

        self._setup_loot_table()

        return ActivitySetupResult(success=True)

    def update_inherited(self) -> ActivityTickResult:
        '''Processing during each tick.'''
        ticks_per_use = self.secateurs.ticks_per_use
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
            msg=f'Collected {items.list_concise()}!',
            items=items,
            xp={
                'foraging': self.herb.xp,
            },
        )

    def finish_inherited(self):
        pass

    def reset_on_levelup(self):
        self._setup_loot_table()

    @property
    def startup_text(self) -> str:
        return f'{self.player} is now collecting {self.herb}.'

    @property
    def standby_text(self) -> str:
        return 'Collecting...'

    @property
    def finish_text(self) -> str:
        return f'{self.player} finished {self.description}.'

    def _setup_loot_table(self):
        foraging_args = {
            'level': self.player.get_level('foraging'),
            'tool': self.secateurs,
        }
        prob_success = self.herb.prob_success(**foraging_args)

        self.loot_table = LootTable()
        self.loot_table.tertiary(
            self.herb.name, prob_success, self.herb.n_per_gather
        )

        # Add more stuff (pets, etc)


def detailed_info():
    msg: list = []

    msg.append('Use cases:')
    msg.append('- collect [item]')

    msg.append('')

    msg.append('Available items:')
    for herb in HERBS:
        name = str(herb).capitalize()
        msg.append(f'- {name}')

    return '\n'.join(msg)
