from ....util.structures.Activity import (
    Activity,
    ActivitySetupResult,
    ActivityMsgType,
    ActivityTickResult
)
from ....util.structures.LootTable import LootTable
from ....util.structures.Bank import Bank
from ....lib.skilling.crafting import craftables, Craftable


class CraftingActivity(Activity):

    def __init__(self, *args):
        super().__init__(*args)

        if self.argument in craftables:
            self.craftable: Craftable = craftables[self.argument]
        else:
            self.craftable: Craftable = None

        self.description: str = 'crafting'

        self.loot_table: LootTable = None

    def setup_inherited(self) -> ActivitySetupResult:
        if self.craftable is None:
            return ActivitySetupResult(
                success=False,
                msg='A valid item was not given.'
            )

        skill_level: int = self.player.get_level('crafting')
        if skill_level < self.craftable.level:
            return ActivitySetupResult(
                success=False,
                msg=f'{self.player} must have Level {self.craftable.level} Crafting to craft a {self.craftable}.'
            )

        for item, quantity in self.craftable.items_required.items():
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
        ticks_per_action = self.craftable.ticks_per_action
        if self.tick_count % ticks_per_action:
            return ActivityTickResult(
                msg=self.standby_text,
                msg_type=ActivityMsgType.WAITING,
            )

        for item, quantity in self.craftable.items_required.items():
            if self.player.has(item, quantity):
                continue

            return ActivityTickResult(
                msg=f'{self.player} ran out of {item}.',
                exit=True,
            )

        # Process the item
        for item, quantity in self.craftable.items_required.items():
            self.player.remove(item, quantity)

        items: Bank = self.loot_table.roll()

        return ActivityTickResult(
            msg=f'Crafted a {self.craftable}!',
            items=items,
            xp={
                'crafting': self.craftable.XP,
            },
        )

    def finish_inherited(self):
        pass

    def reset_on_levelup(self):
        self._setup_loot_table()

    @property
    def startup_text(self) -> str:
        return f'{self.player} is now crafting a {self.craftable}.'

    @property
    def standby_text(self) -> str:
        return 'Crafting...'

    @property
    def finish_text(self) -> str:
        return f'{self.player} finished {self.description}.'

    def _setup_loot_table(self):
        self.loot_table = LootTable()
        self.loot_table.every(
            self.craftable.name, 1
        )

        # Add more stuff (pets, etc)


def detailed_info():
    msg: list = []

    msg.append('Use cases:')
    msg.append('- craft [item]')

    msg.append('')

    msg.append('Available items:')
    for craftable in craftables:
        name = str(craftable).capitalize()
        msg.append(f'- {name}')

    return '\n'.join(msg)
