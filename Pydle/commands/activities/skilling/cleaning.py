from ....util.structures.Activity import (
    Activity,
    ActivitySetupResult,
    ActivityMsgType,
    ActivityTickResult
)
from ....util.structures.LootTable import LootTable
from ....util.structures.Bank import Bank
from ....lib.skilling.herblore import cleanables, Cleanable


ticks_per_clean = 2


class CleaningActivity(Activity):

    def __init__(self, *args):
        super().__init__(*args)

        if self.argument in cleanables:
            self.cleanable: Cleanable = cleanables[self.argument]
        else:
            self.cleanable: Cleanable = None

        self.description: str = 'cleaning'

        self.loot_table: LootTable = None

    def setup_inherited(self) -> ActivitySetupResult:
        if self.cleanable is None:
            return ActivitySetupResult(
                success=False,
                msg='A valid item was not given.'
            )

        skill_level: int = self.player.get_level('herblore')
        if skill_level < self.cleanable.level:
            return ActivitySetupResult(
                success=False,
                msg=f'{self.player} must have Level {self.cleanable.level} Herblore to clean a {self.cleanable}.'
            )

        for item, quantity in self.cleanable.items_required.items():
            if self.player.has(item, quantity):
                continue

            return ActivitySetupResult(
                success=False,
                msg=f'{self.player} does not have {quantity}x {item}.'
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

        for item, quantity in self.cleanable.items_required.items():
            if self.player.has(item, quantity):
                continue

            return ActivityTickResult(
                msg=f'{self.player} ran out of {item}.',
                exit=True,
            )

        # Process the item
        for item, quantity in self.cleanable.items_required.items():
            self.player.remove(item, quantity)

        items: Bank = self.loot_table.roll()

        return ActivityTickResult(
            msg=f'Cleaned {self.cleanable}!',
            items=items,
            xp={
                'herblore': self.cleanable.XP,
            },
        )

    def finish_inherited(self):
        pass

    def reset_on_levelup(self):
        self._setup_loot_table()

    @property
    def startup_text(self) -> str:
        return f'{self.player} is now cleaning {self.cleanable}.'

    @property
    def standby_text(self) -> str:
        return 'Cleaning...'

    @property
    def finish_text(self) -> str:
        return f'{self.player} finished {self.description}.'

    def _setup_loot_table(self):
        self.loot_table = LootTable()
        self.loot_table.every(
            self.cleanable.name, 1
        )

        # Add more stuff (pets, etc)


def detailed_info():
    msg: list = []

    msg.append('Use cases:')
    msg.append('- clean [herb]')

    msg.append('')

    msg.append('Available herbs:')
    for cleanable in cleanables:
        name = str(cleanable).capitalize()
        msg.append(f'- {name}')

    return '\n'.join(msg)
