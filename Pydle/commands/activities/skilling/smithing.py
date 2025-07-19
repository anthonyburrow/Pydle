from ....util.structures.Activity import (
    Activity,
    ActivitySetupResult,
    ActivityMsgType,
    ActivityTickResult
)
from ....util.structures.LootTable import LootTable
from ....util.structures.Bank import Bank
from ....lib.skilling.smithing import smithables, Smithable
from ....lib.skilling.woodcutting import logs


fire_effect = 'smithing fire'


class SmithingActivity(Activity):

    def __init__(self, *args):
        super().__init__(*args)

        if self.argument in smithables:
            self.smithable: Smithable = smithables[self.argument]
        else:
            self.smithable: Smithable = None

        self.description: str = 'smithing'

        self.loot_table: LootTable = None

    def setup_inherited(self) -> ActivitySetupResult:
        if self.smithable is None:
            return ActivitySetupResult(
                success=False,
                msg='A valid item was not given.'
            )

        skill_level: int = self.player.get_level('smithing')
        if skill_level < self.smithable.level:
            return ActivitySetupResult(
                success=False,
                msg=f'{self.player} must have Level {self.smithable.level} Smithing to smith a {self.smithable.name}.'
            )

        if not self.player.has_effect(fire_effect):
            for log_key, log in logs.items():
                if self.player.has(log.name):
                    break
            else:
                return ActivitySetupResult(
                    success=False,
                    msg=f'{self.player} has no logs to fuel a furnace.'
                )

        for item, quantity in self.smithable.items_required.items():
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
        ticks_per_action = self.smithable.ticks_per_action
        if self.tick_count % ticks_per_action:
            return ActivityTickResult(
                msg=self.standby_text,
                msg_type=ActivityMsgType.WAITING,
            )

        for item, quantity in self.smithable.items_required.items():
            if self.player.has(item, quantity):
                continue

            return ActivityTickResult(
                msg=f'{self.player} ran out of {item}.',
                exit=True,
            )

        if not self.player.has_effect(fire_effect):
            for log_key, log in logs.items():
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
        for item, quantity in self.smithable.items_required.items():
            self.player.remove(item, quantity)

        items: Bank = self.loot_table.roll()

        return ActivityTickResult(
            msg=f'Smithed a {self.smithable.name}!',
            items=items,
            xp={
                'smithing': self.smithable.XP,
            },
        )

    def finish_inherited(self):
        pass

    def reset_on_levelup(self):
        self._setup_loot_table()

    @property
    def startup_text(self) -> str:
        return f'{self.player} is now smithing a {self.smithable.name}.'

    @property
    def standby_text(self) -> str:
        return 'Smithing...'

    @property
    def finish_text(self) -> str:
        return f'{self.player} finished {self.description}.'

    def _setup_loot_table(self):
        self.loot_table = LootTable()
        self.loot_table.every(
            self.smithable.name, 1
        )

        # Add more stuff (pets, etc)


def detailed_info():
    msg: list = []

    msg.append('Use cases:')
    msg.append('- smith [item]')

    msg.append('')

    msg.append('Available items:')
    for smithable in smithables:
        name = str(smithable).capitalize()
        msg.append(f'- {name}')

    return '\n'.join(msg)
