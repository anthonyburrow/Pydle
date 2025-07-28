from ....util.structures.Activity import (
    Activity,
    ActivitySetupResult,
    ActivityMsgType,
    ActivityTickResult
)
from ....util.structures.LootTable import LootTable
from ....util.structures.Bank import Bank
from ....lib.skilling.cooking import Cookable, COOKABLES
from ....lib.skilling.woodcutting import LOGS


fire_effect = 'cooking fire'


class CookingActivity(Activity):

    def __init__(self, *args):
        super().__init__(*args)

        if self.argument in COOKABLES:
            self.cookable: Cookable = COOKABLES[self.argument]
        else:
            self.cookable: Cookable = None

        self.description: str = 'cooking'

        self.loot_table: LootTable = None

    def setup_inherited(self) -> ActivitySetupResult:
        if self.cookable is None:
            return ActivitySetupResult(
                success=False,
                msg='A valid item was not given.'
            )

        skill_level: int = self.player.get_level('cooking')
        if skill_level < self.cookable.level:
            return ActivitySetupResult(
                success=False,
                msg=f'{self.player} must have Level {self.cookable.level} Cooking to cook {self.cookable}.'
            )

        if not self.player.has_effect(fire_effect):
            for log_key, log in LOGS.items():
                if self.player.has(log.name):
                    break
            else:
                return ActivitySetupResult(
                    success=False,
                    msg=f'{self.player} has no logs to make a fire.'
                )

        for item, quantity in self.cookable.items_required.items():
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
        ticks_per_action = self.cookable.ticks_per_action
        if self.tick_count % ticks_per_action:
            return ActivityTickResult(
                msg=self.standby_text,
                msg_type=ActivityMsgType.WAITING,
            )

        for item, quantity in self.cookable.items_required.items():
            if self.player.has(item, quantity):
                continue

            return ActivityTickResult(
                msg=f'{self.player} ran out of {item}.',
                exit=True,
            )

        if not self.player.has_effect(fire_effect):
            for log_key, log in LOGS.items():
                if self.player.has(log.name):
                    self.player.remove(log.name, 1)
                    self.player.add_effect(fire_effect, log.ticks_per_fire)
                    break
            else:
                return ActivityTickResult(
                    msg=f'{self.player} ran out of logs.',
                    exit=True,
                )

        # Process the item
        for item, quantity in self.cookable.items_required.items():
            self.player.remove(item, quantity)

        items: Bank = self.loot_table.roll()
        if not items:
            return ActivityTickResult(
                msg=f'Burned {self.cookable}...',
                xp={
                    'cooking': self.cookable.xp * 0.5,
                },
            )

        return ActivityTickResult(
            msg=f'Cooked {self.cookable}!',
            items=items,
            xp={
                'cooking': self.cookable.xp,
            },
        )

    def finish_inherited(self):
        pass

    def reset_on_levelup(self):
        self._setup_loot_table()

    @property
    def startup_text(self) -> str:
        return f'{self.player} is now cooking {self.cookable}.'

    @property
    def standby_text(self) -> str:
        return 'Cooking...'

    @property
    def finish_text(self) -> str:
        return f'{self.player} finished {self.description}.'

    def _setup_loot_table(self):
        cooking_args = (
            self.player.get_level('cooking'),
        )
        prob_success = self.cookable.prob_success(*cooking_args)

        self.loot_table = LootTable()
        self.loot_table.tertiary(
            self.cookable.name, prob_success, 1
        )

        # Add more stuff (pets, etc)


def detailed_info():
    msg: list = []

    msg.append('Use cases:')
    msg.append('- cook [food]')

    msg.append('')

    msg.append('Available foods:')
    for cookable in COOKABLES:
        name = str(cookable).capitalize()
        msg.append(f'- {name}')

    return '\n'.join(msg)
