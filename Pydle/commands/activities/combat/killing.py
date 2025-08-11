from ...Activity import (
    Activity,
    ActivityCheckResult,
    ActivityMsgType,
    ActivityTickResult
)
from ....lib.areas import AREAS
from ....util.monsters.Monster import Monster
from ....util.monsters.MonsterInstance import MonsterInstance
from ....util.player.Bank import Bank
from ....util.player.EquipmentSlot import EquipmentSlot
from ....util.structures.Area import Area
from ....util.structures.CombatEngine import CombatEngine


class KillingActivity(Activity):

    name: str = 'kill'
    help_info: str = 'Begin killing a monster.'

    def __init__(self, *args):
        super().__init__(*args)

        self.monster: MonsterInstance | None = self.command.get_monster_instance()
        self.combat_engine: CombatEngine = CombatEngine(self.player, self.monster)

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

    def check(self) -> ActivityCheckResult:
        result: ActivityCheckResult = super().check()
        if not result.success:
            return result

        if self.monster is None:
            return ActivityCheckResult(
                success=False,
                msg='A valid monster was not given.'
            )

        if not isinstance(self.monster.base, Monster):
            return ActivityCheckResult(
                success=False,
                msg=f'{self.monster} is not a valid monster.'
            )

        area: Area = AREAS[self.player.area]
        if not area.contains_monster(self.monster):
            return ActivityCheckResult(
                success=False,
                msg=f'{area} does not have a {self.monster} anywhere.'
            )

        if not self.player.equipment[EquipmentSlot.WEAPON]:
            return ActivityCheckResult(
                success=False,
                msg=f'{self.player} needs a weapon to fight!'
            )

        # Checks for:
        #   - "slayer" level/rank
        #   - items required to do monster/boss

        return ActivityCheckResult(success=True)

    def begin(self) -> None:
        super().begin()

    def _process_tick(self) -> ActivityTickResult:
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

    def _recheck(self) -> ActivityCheckResult:
        result: ActivityCheckResult = super()._recheck()
        if not result.success:
            return result

        if self.player.hitpoints <= 0:
            return ActivityCheckResult(
                success=False,
                msg=f'{self.player} was defeated.',
            )

        return ActivityCheckResult(success=True)

    def finish(self) -> None:
        super().finish()

        self.player.heal_full()

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
        return f'{self.player} finished killing {self.monster}.'

    def _on_levelup(self):
        super()._on_levelup()

        self.combat_engine.calculate_values()
