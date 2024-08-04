from ....util.structures.Activity import Activity, Status
from ....util.structures.LootTable import LootTable
from ....util.structures.Bank import Bank
from ....lib.skilling.foraging import herbs, Herb


ticks_per_clean = 2


class CleaningActivity(Activity):

    def __init__(self, *args):
        super().__init__(*args)

        self.herb: Herb = None
        self.parse_args(*args[1:])

        self.description: str = 'cleaning'

        self.loot_table: LootTable = None

    def parse_args(self, *args, **kwargs):
        '''
        Accepted command styles:
            clean 'herb'
        '''
        try:
            self.herb: Herb = herbs[args[0]]
        except (IndexError, KeyError):
            self.herb: Herb = None

    def setup_inherited(self, status: dict) -> dict:
        if self.herb is None:
            status['success'] = False
            status['msg'] = \
                'A valid item was not given.'
            return status

        skill_level: int = self.player.get_level('herblore')
        if skill_level < self.herb.level:
            status['success'] = False
            status['msg'] = \
                f'{self.player} must have Level {self.herb.level} Herblore to clean a {self.herb.name_clean}.'
            return status

        if not self.player.has(self.herb.name_grimy):
            msg = f'{self.player} does not have any {self.herb.name_grimy}.'
            status['success'] = False
            status['msg'] = msg
            return status

        self._setup_loot_table()

        return status

    def update_inherited(self) -> dict:
        '''Processing during each tick.'''
        # Do checks
        if self.tick_count % ticks_per_clean:
            return {
                'status': Status.STANDBY,
                'msg': self.standby_text,
            }

        if not self.player.has(self.herb.name_grimy):
            msg = f'{self.player} ran out of {self.herb.name_grimy} to clean.'
            return {
                'status': Status.EXIT,
                'msg': msg,
            }

        # Process the item
        self.player.remove(self.herb.name_grimy, 1)

        items: Bank = self.loot_table.roll()

        msg = f'Cleaned {self.herb.name_clean}!'

        return {
            'status': Status.ACTIVE,
            'msg': msg,
            'items': items,
            'XP': {
                'herblore': self.herb.XP_clean,
            },
        }

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
