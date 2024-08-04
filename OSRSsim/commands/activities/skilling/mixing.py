from ....util.structures.Activity import Activity, Status
from ....util.structures.LootTable import LootTable
from ....util.structures.Bank import Bank
from ....lib.skilling.herblore import mixables, Mixable


class MixingActivity(Activity):

    def __init__(self, *args):
        super().__init__(*args)

        self.mixable: Mixable = None
        self.parse_args(*args[1:])

        self.description: str = 'mixing'

        self.loot_table: LootTable = None

    def parse_args(self, *args, **kwargs):
        '''
        Accepted command styles:
            mix 'potion'
        '''
        try:
            self.mixable: Mixable = mixables[args[0]]
        except (IndexError, KeyError):
            self.mixable: Mixable = None

    def setup_inherited(self, status: dict) -> dict:
        if self.mixable is None:
            status['success'] = False
            status['msg'] = \
                'A valid item was not given.'
            return status

        skill_level: int = self.player.get_level('herblore')
        if skill_level < self.mixable.level:
            status['success'] = False
            status['msg'] = \
                f'{self.player} must have Level {self.mixable.level} Herblore to mix a {self.mixable.name}.'
            return status

        for item, quantity in self.mixable.items_required.items():
            if self.player.has(item, quantity):
                continue

            msg = f'{self.player} does not have any {item}.'
            status['success'] = False
            status['msg'] = msg
            return status

        self._setup_loot_table()

        return status

    def update_inherited(self) -> dict:
        '''Processing during each tick.'''
        # Do checks
        ticks_per_action = self.mixable.ticks_per_action
        if self.tick_count % ticks_per_action:
            return {
                'status': Status.STANDBY,
                'msg': self.standby_text,
            }

        for item, quantity in self.mixable.items_required.items():
            if self.player.has(item, quantity):
                continue

            msg = f'{self.player} ran out of {item}.'
            return {
                'status': Status.EXIT,
                'msg': msg,
            }

        # Process the item
        for item, quantity in self.mixable.items_required.items():
            self.player.remove(item, quantity)

        items: Bank = self.loot_table.roll()

        msg = f'Mixed a {self.mixable.name}!'

        return {
            'status': Status.ACTIVE,
            'msg': msg,
            'items': items,
            'XP': {
                'herblore': self.mixable.XP,
            },
        }

    def finish_inherited(self):
        pass

    def reset_on_levelup(self):
        self._setup_loot_table()

    @property
    def startup_text(self) -> str:
        return f'{self.player} is now mixing {self.mixable.name}s.'

    @property
    def standby_text(self) -> str:
        return 'Mixing...'

    @property
    def finish_text(self) -> str:
        return f'{self.player} finished {self.description}.'

    def _setup_loot_table(self):
        self.loot_table = LootTable()
        self.loot_table.every(
            self.mixable.name, self.mixable.n_doses
        )

        # Add more stuff (pets, etc)


def detailed_info():
    msg: list = []

    msg.append('Use cases:')
    msg.append('- mix [potion]')

    msg.append('')

    msg.append('Available potions:')
    for mixable in mixables:
        name = str(mixable).capitalize()
        msg.append(f'- {name}')

    return '\n'.join(msg)
