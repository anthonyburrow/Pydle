from ....util.structures.Activity import (
    Activity,
    ActivitySetupResult,
    ActivityMsgType,
    ActivityTickResult
)
from ....util.structures.Bank import Bank
from ....util.structures.Monster import Monster
from ....util.structures.CombatEngine import CombatEngine
from ....lib.monsters import monsters


class KillingActivity(Activity):

    def __init__(self, *args):
        super().__init__(*args)

        if self.argument in monsters:
            monster_args = monsters[self.argument]
            self.monster: Monster = Monster(**monster_args)
        else:
            self.monster: Monster = None

        self.description: str = 'killing'
        self.combat_engine: CombatEngine = CombatEngine(self.player, self.monster)

    def setup_inherited(self) -> ActivitySetupResult:
        if self.monster is None:
            return ActivitySetupResult(
                success=False,
                msg='A valid monster was not given.'
            )

        if self.player.equipment['weapon'] is None:
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
        # Do checks
        if self.player.hitpoints <= 0:
            return ActivityTickResult(
                msg=f'{self.player} was defeated.',
                exit=True,
            )

        if self.monster.hitpoints <= 0:
            items: Bank = self.monster.loot_table.roll()

            self.monster.reset()

            return ActivityTickResult(
                msg=f'Killed {self.monster}!',
                items=items,
            )

        # Processing
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

    def reset_on_levelup(self):
        # Recalculate hit chance/max hit on levelup
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


def detailed_info():
    msg: list = []

    msg.append('Use cases:')
    msg.append('- kill [monster]')

    # msg.append('')

    # msg.append('Available monsters:')
    # for monster in monsters:
    #     name = str(monster['name']).capitalize()
    #     msg.append(f'- {name}')

    return '\n'.join(msg)
