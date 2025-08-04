from ....util.structures.Activity import (
    Activity,
    ActivitySetupResult,
    ActivityMsgType,
    ActivityTickResult
)
from ....util.structures.LootTable import LootTable
from ....util.structures.Bank import Bank
from ....util.items.skilling.Mixable import Mixable
from ....lib.skilling.herblore import MIXABLES


class MixingActivity(Activity):

    def __init__(self, *args):
        super().__init__(*args)

        if self.argument in MIXABLES:
            self.mixable: Mixable = MIXABLES[self.argument]
        else:
            self.mixable: Mixable = None

        self.description: str = 'mixing'

        self.loot_table: LootTable = None

    def setup_inherited(self) -> ActivitySetupResult:
        if self.mixable is None:
            return ActivitySetupResult(
                success=False,
                msg='A valid item was not given.'
            )

        skill_level: int = self.player.get_level('herblore')
        if skill_level < self.mixable.level:
            return ActivitySetupResult(
                success=False,
                msg=f'{self.player} must have Level {self.mixable.level} Herblore to mix a {self.mixable}.'
            )

        for item, quantity in self.mixable.items_required.items():
            if self.player.has(item, quantity):
                continue

            return ActivitySetupResult(
                success=False,
                msg=f'{self.player} does not have any {item}.'
            )

        self._setup_loot_table()

        return ActivitySetupResult(success=True)

    def update_inherited(self) -> ActivityTickResult:
        '''Processing during each tick.'''
        # Do checks
        ticks_per_action = self.mixable.ticks_per_action
        if self.tick_count % ticks_per_action:
            return ActivityTickResult(
                msg=self.standby_text,
                msg_type=ActivityMsgType.WAITING,
            )

        for item, quantity in self.mixable.items_required.items():
            if self.player.has(item, quantity):
                continue

            return ActivityTickResult(
                msg=f'{self.player} ran out of {item}.',
                exit=True,
            )

        # Process the item
        for item, quantity in self.mixable.items_required.items():
            self.player.remove(item, quantity)

        items: Bank = self.loot_table.roll()

        return ActivityTickResult(
            msg=f'Mixed a {self.mixable}!',
            items=items,
            xp={
                'herblore': self.mixable.xp,
            },
        )

    def finish_inherited(self):
        pass

    def reset_on_levelup(self):
        self._setup_loot_table()

    @property
    def startup_text(self) -> str:
        return f'{self.player} is now mixing a {self.mixable}.'

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
    for mixable in MIXABLES:
        name = str(mixable).capitalize()
        msg.append(f'- {name}')

    return '\n'.join(msg)
