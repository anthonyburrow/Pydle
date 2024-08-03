from ....util.structures.Activity import Activity, Status
from ....util.structures.LootTable import LootTable
from ....util.structures.Bank import Bank
from ...data.skilling.crafting import craftables, Craftable


class CraftingActivity(Activity):

    def __init__(self, *args):
        super().__init__(*args)

        self.craftable: Craftable = None
        self.parse_args(*args[1:])

        self.description: str = 'crafting'

        self.loot_table: LootTable = None

    def parse_args(self, *args, **kwargs):
        '''
        Accepted command styles:
            craft 'item'
        '''
        try:
            self.craftable: Craftable = craftables[' '.join(args)]
        except (IndexError, KeyError):
            self.craftable: Craftable = None

    def setup_inherited(self, status: dict) -> dict:
        if self.craftable is None:
            status['success'] = False
            status['msg'] = \
                'A valid item was not given.'
            return status

        skill_level: int = self.player.get_level('crafting')
        if skill_level < self.craftable.level:
            status['success'] = False
            status['msg'] = \
                f'{self.player} must have Level {self.craftable.level} Crafting to craft a {self.craftable.name}.'
            return status

        for item, quantity in self.craftable.items_required.items():
            if self.player.has(item, quantity):
                continue

            msg = f'{self.player} does not have {quantity}x {item}.'
            status['success'] = False
            status['msg'] = msg
            return status

        self._setup_loot_table()

        return status

    def update_inherited(self) -> dict:
        '''Processing during each tick.'''
        # Do checks
        ticks_per_action = self.craftable.ticks_per_action
        if self.tick_count % ticks_per_action:
            return {
                'status': Status.STANDBY,
                'msg': self.standby_text,
            }

        for item, quantity in self.craftable.items_required.items():
            if self.player.has(item, quantity):
                continue

            msg = f'{self.player} ran out of {item}.'
            return {
                'status': Status.EXIT,
                'msg': msg,
            }

        # Process the item
        for item, quantity in self.craftable.items_required.items():
            self.player.remove(item, quantity)

        items: Bank = self.loot_table.roll()

        msg = f'Crafted a {self.craftable.name}!'

        return {
            'status': Status.ACTIVE,
            'msg': msg,
            'items': items,
            'XP': {
                'crafting': self.craftable.XP,
            },
        }

    def finish_inherited(self):
        pass

    def reset_on_levelup(self):
        self._setup_loot_table()

    @property
    def startup_text(self) -> str:
        return f'{self.player} is now crafting a {self.craftable.name}.'

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
