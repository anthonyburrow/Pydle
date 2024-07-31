from ....util.structures.Activity import Activity, Status
from ....util.structures.LootTable import LootTable
from ....util.structures.Bank import Bank
from ...data.skilling.smithing import smeltables, Smeltable
from ...data.skilling.woodcutting import logs


fire_effect = 'smithing fire'


class SmeltingActivity(Activity):

    def __init__(self, *args):
        super().__init__(*args)

        self.smeltable: Smeltable = None
        self.parse_args(*args[1:])

        self.description: str = 'smelting'

        self.loot_table: LootTable = None

    def parse_args(self, *args, **kwargs):
        '''
        Accepted command styles:
            smelt 'ore'
        '''
        try:
            self.smeltable: Smeltable = smeltables[args[0]]
        except (IndexError, KeyError):
            self.smeltable: Smeltable = None

    def setup_inherited(self, status: dict) -> dict:
        if self.smeltable is None:
            status['success'] = False
            status['msg'] = \
                'A valid item was not given.'
            return status

        skill_level: int = self.player.get_level('smithing')
        if skill_level < self.smeltable.level:
            status['success'] = False
            status['msg'] = \
                f'{self.player} must have Level {self.smeltable.level} Smithing to smelt a {self.smeltable.name}.'
            return status

        if not self.player.has_effect(fire_effect):
            for log_key, log in logs.items():
                if self.player.has(log.name):
                    break
            else:
                status['success'] = False
                status['msg'] = \
                    f'{self.player} has no logs to fuel a furnace.'
                return status

        for item, quantity in self.smeltable.items_required.items():
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
        ticks_per_action = self.smeltable.ticks_per_action
        if self.tick_count % ticks_per_action:
            return {
                'status': Status.STANDBY,
                'msg': self.standby_text,
            }

        for item, quantity in self.smeltable.items_required.items():
            if self.player.has(item, quantity):
                continue

            msg = f'{self.player} ran out of {item}.'
            return {
                'status': Status.EXIT,
                'msg': msg,
            }

        if not self.player.has_effect(fire_effect):
            for log_key, log in logs.items():
                if self.player.has(log.name):
                    self.player.remove(log.name, 1)
                    self.player.add_effect(fire_effect, log.ticks_per_fire)
                    break
            else:
                msg = f'{self.player} ran out of logs.'
                return {
                    'status': Status.EXIT,
                    'msg': msg,
                }

        # Process the item
        for item, quantity in self.smeltable.items_required.items():
            self.player.remove(item, quantity)

        items: Bank = self.loot_table.roll()

        msg = f'Smelted a {self.smeltable.name}!'

        return {
            'status': Status.ACTIVE,
            'msg': msg,
            'items': items,
            'XP': {
                'smithing': self.smeltable.XP,
            },
        }

    def finish_inherited(self):
        pass

    def reset_on_levelup(self):
        self._setup_loot_table()

    @property
    def startup_text(self) -> str:
        return f'{self.player} is now smelting a {self.smeltable.name}.'

    @property
    def standby_text(self) -> str:
        return 'Smelting...'

    @property
    def finish_text(self) -> str:
        return f'{self.player} finished {self.description}.'

    def _setup_loot_table(self):
        self.loot_table = LootTable()
        self.loot_table.every(
            self.smeltable.name, 1
        )

        # Add more stuff (pets, etc)
