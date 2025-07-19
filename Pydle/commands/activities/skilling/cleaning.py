from ....util.structures.Activity import (
    Activity,
    ActivitySetupResult,
    ActivityMsgType,
    ActivityTickResult
)
from ....util.structures.LootTable import LootTable
from ....util.structures.Bank import Bank
from ....lib.skilling.foraging import herbs, Herb


ticks_per_clean = 2


class CleaningActivity(Activity):

    def __init__(self, *args):
        super().__init__(*args)

        if self.argument in herbs:
            self.herb: Herb = herbs[self.argument]
        else:
            self.herb: Herb = None

        self.description: str = 'cleaning'

        self.loot_table: LootTable = None

    def setup_inherited(self) -> ActivitySetupResult:
        if self.herb is None:
            return ActivitySetupResult(
                success=False,
                msg='A valid item was not given.'
            )

        skill_level: int = self.player.get_level('herblore')
        if skill_level < self.herb.level:
            return ActivitySetupResult(
                success=False,
                msg=f'{self.player} must have Level {self.herb.level} Herblore to clean a {self.herb.name_clean}.'
            )

        if not self.player.has(self.herb.name_grimy):
            return ActivitySetupResult(
                success=False,
                msg=f'{self.player} does not have any {self.herb.name_grimy}.'
            )

        self._setup_loot_table()

        return ActivitySetupResult(success=True)

    def update_inherited(self) -> ActivityTickResult:
        '''Processing during each tick.'''
        # Do checks
        if self.tick_count % ticks_per_clean:
            return ActivityTickResult(
                msg=self.standby_text,
                msg_type=ActivityMsgType.WAITING,
            )

        if not self.player.has(self.herb.name_grimy):
            return ActivityTickResult(
                msg=f'{self.player} ran out of {self.herb.name_grimy} to clean.',
                exit=True,
            )

        # Process the item
        self.player.remove(self.herb.name_grimy, 1)

        items: Bank = self.loot_table.roll()

        msg = f'Cleaned {self.herb.name_clean}!'

        return ActivityTickResult(
            msg=msg,
            items=items,
            xp={
                'herblore': self.herb.XP_clean,
            },
        )

    def finish_inherited(self):
        pass

    def reset_on_levelup(self):
        self._setup_loot_table()

    @property
    def startup_text(self) -> str:
        return f'{self.player} is now cleaning {self.herb.name_clean}.'

    @property
    def standby_text(self) -> str:
        return 'Cleaning...'

    @property
    def finish_text(self) -> str:
        return f'{self.player} finished {self.description}.'

    def _setup_loot_table(self):
        self.loot_table = LootTable()
        self.loot_table.every(
            self.herb.name_clean, 1
        )

        # Add more stuff (pets, etc)


def detailed_info():
    msg: list = []

    msg.append('Use cases:')
    msg.append('- clean [herb]')

    msg.append('')

    msg.append('Available herbs:')
    for herb in herbs:
        name = str(herb).capitalize()
        msg.append(f'- {name}')

    return '\n'.join(msg)
