from ....lib.areas import AREAS
from ....util.monsters.Monster import Monster
from ....util.monsters.MonsterInstance import MonsterInstance
from ....util.player.Bank import Bank
from ....util.player.EquipmentSlot import EquipmentSlot
from ....util.structures.Activity import (
    Activity,
    ActivitySetupResult,
    ActivityMsgType,
    ActivityTickResult
)
from ....util.structures.Area import Area
from ....util.structures.CombatEngine import CombatEngine


class KillingActivity(Activity):

    name: str = 'kill'
    help_info: str = 'Begin killing a monster.'

    def __init__(self, *args):
        super().__init__(*args)

        self.monster: MonsterInstance | None = self.command.get_monster_instance()
        self.combat_engine: CombatEngine = CombatEngine(self.player, self.monster)

        self.description: str = 'killing'

    @classmethod
    def usage(cls) -> str:
        msg: list[str] = []

        msg.append('Use cases:')
        msg.append('- kill [monster]')

        # msg.append('')

        # msg.append('Available monsters:')
        # for monster in MONSTERS:
        #     name = str(monster['name']).capitalize()
        #     msg.append(f'- {name}')

        return '\n'.join(msg)

    def setup_inherited(self) -> ActivitySetupResult:
        if self.monster is None:
            return ActivitySetupResult(
                success=False,
                msg='A valid monster was not given.'
            )

        if not isinstance(self.monster.base, Monster):
            return ActivitySetupResult(
                success=False,
                msg=f'{self.monster} is not a valid monster.'
            )

        area: Area = AREAS[self.player.area]
        if not area.contains_monster(self.monster):
            return ActivitySetupResult(
                success=False,
                msg=f'{area} does not have a {self.monster} anywhere.'
            )

        if not self.player.equipment[EquipmentSlot.WEAPON]:
            return ActivitySetupResult(
                success=False,
                msg=f'{self.player} needs a weapon to fight!'
            )

        # Checks for:
        #   - "slayer" level/rank
        #   - items required to do monster/boss

        return ActivitySetupResult(success=True)

    def update_inherited(self) -> ActivityTickResult:
        '''Processing during each tick.'''
        if self.player.hitpoints <= 0:
            return ActivityTickResult(
                msg=f'{self.player} was defeated.',
                exit=True,
            )

        if self.monster.hitpoints <= 0:
            items: Bank = self.monster.loot_table.roll()

            # Make new monster instance when killed
            self.monster = self.command.get_monster_instance()

            return ActivityTickResult(
                msg=f'Killed {self.monster}!',
                items=items,
            )

        result_combat = self.combat_engine.tick(self.tick_count)
        if not result_combat:
            return ActivityTickResult(
                msg=self.standby_text,
                msg_type=ActivityMsgType.WAITING
            )

        player_damage_str: str = \
            f'-{result_combat.player_damage}' if result_combat.player_damage else ''
        monster_damage_str: str = \
            f'-{result_combat.monster_damage}' if result_combat.monster_damage else ''

        msg = (
            f'{self.player} ({self.player.hitpoints}) {player_damage_str}  |  '
            f'{self.monster} ({self.monster.hitpoints}) {monster_damage_str}'
        )

        return ActivityTickResult(
            msg=msg,
            xp=result_combat.xp,
        )

    def finish_inherited(self):
        self.player.heal_full()

    def _on_levelup(self):
        self.combat_engine.calculate_values()

    @property
    def startup_text(self) -> str:
        return f'{self.player} is now fighting {self.monster}.'

    @property
    def standby_text(self) -> str:
        return 'Fighting...'

    @property
    def finish_text(self) -> str:
        if self.player.hitpoints <= 0:
            return ''
        return f'{self.player} finished {self.description}.'
