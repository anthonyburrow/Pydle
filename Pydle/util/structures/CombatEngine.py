from dataclasses import dataclass

from .Player import Player
from .Monster import Monster


@dataclass
class CombatResult:
    player_damage: int
    monster_damage: int
    xp: dict


class CombatEngine:
    def __init__(self, player: Player, monster: Monster):
        self.player: Player = player
        self.monster: Monster = monster

    def tick(self, tick_count: int) -> CombatResult | None:
        monster_speed: int = self.monster.get_stat('ticks_per_action')
        player_speed: int = self.player.get_stat('ticks_per_action')

        player_attacks: bool = tick_count % player_speed == 0
        monster_attacks: bool = (tick_count - 1) % monster_speed == 0

        if not player_attacks and not monster_attacks:
            return None

        xp: dict = {}
        player_damage: int = 0
        monster_damage: int = 0

        xp_per_dmg = 2.

        if monster_attacks:
            player_damage: int = self.calculate_damage(
                attacker=self.monster, defender=self.player
            )
            player_damage = min(player_damage, self.player.hitpoints)
            self.player.damage(player_damage)
            xp['defense'] = float(player_damage) * xp_per_dmg

        if player_attacks:
            monster_damage: int = self.calculate_damage(
                attacker=self.player, defender=self.monster
            )
            monster_damage = min(monster_damage, self.monster.hitpoints)
            self.monster.damage(monster_damage)
            xp['attack'] = float(monster_damage) * xp_per_dmg

        return CombatResult(
            player_damage=player_damage,
            monster_damage=monster_damage,
            xp=xp
        )

    def calculate_damage(
        self,
        attacker: Player | Monster,
        defender: Player | Monster,
    ) -> int:
        # Eventually include accuracy, crits, armor, etc.
        return 1
