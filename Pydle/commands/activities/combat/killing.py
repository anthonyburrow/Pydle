from ....util.structures.Activity import (
    Activity,
    ActivitySetupResult,
    ActivityMsgType,
    ActivityTickResult
)
from ....util.structures.Bank import Bank
from ....lib.monsters import monsters, Monster


class KillingActivity(Activity):

    def __init__(self, *args):
        super().__init__(*args)

        if self.argument in monsters:
            monster_args = monsters[self.argument]
            self.monster: Monster = Monster(**monster_args)
        else:
            self.monster: Monster = None

        self.description: str = 'killing'

    def setup_inherited(self) -> ActivitySetupResult:
        if self.monster is None:
            return ActivitySetupResult(
                success=False,
                msg='A valid monster was not given.'
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
        monster_tick_speed = self.monster.get_stat('ticks_per_action')
        monster_attacking = not (self.tick_count - 1) % monster_tick_speed

        player_tick_speed = self.player.get_stat('ticks_per_action')
        player_attacking = not self.tick_count % player_tick_speed

        if not (monster_attacking or player_attacking):
            return ActivityTickResult(
                msg=self.standby_text,
                # msg_type=ActivityMsgType.WAITING,
                msg_type=ActivityMsgType.RESULT,
            )

        xp = {}

        player_damage: int = 0
        monster_damage: int = 0

        if monster_attacking:
            damage: int = 1
            player_damage = min(damage, self.player.hitpoints)
            self.player.damage(player_damage)
            xp['defense'] = 2. * float(player_damage)

        if player_attacking:
            damage: int = 20
            monster_damage = min(damage, self.monster.hitpoints)
            self.monster.damage(monster_damage)
            xp['attack'] = 2. * float(monster_damage)

        player_damage_str: str = f'-{player_damage}' if player_damage else ''
        monster_damage_str: str = f'-{monster_damage}' if monster_damage else ''

        msg = (
            f'{self.player} ({self.player.hitpoints}) {player_damage_str}  |  '
            f'{self.monster} ({self.monster.hitpoints}) {monster_damage_str}')

        return ActivityTickResult(
            msg=msg,
            xp=xp,
        )

    def finish_inherited(self):
        self.player.heal_full()

    def reset_on_levelup(self):
        pass

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
