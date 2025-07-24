from numpy.random import rand, randint
from numpy import exp
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

        self.player_hit_chance: float = 0.
        self.player_max_hit: int = 1

        self.monster_hit_chance: float = 0.
        self.monster_max_hit: int = 1

        self.calculate_values()

    def calculate_values(self):
        # Player hit chance
        accuracy: int = self._calculate_effective_level(
            self.player.get_level('attack'),
            self.player.get_stat('accuracy')
        )

        evasiveness: int = self.monster.get_stat('evasiveness')

        self.player_hit_chance = self._calculate_hit_chance(
            accuracy, evasiveness
        )

        # Monster hit chance
        accuracy: int = self.monster.get_stat('accuracy')

        evasiveness: int = self._calculate_effective_level(
            self.player.get_level('evasiveness'),
            self.player.get_stat('evasiveness')
        )

        self.monster_hit_chance = self._calculate_hit_chance(
            accuracy, evasiveness
        )

        # Player max hit
        physical_strength: int = self._calculate_effective_level(
            self.player.get_level('strength'),
            self.player.get_stat('physical_strength')
        )
        magical_power: int = self._calculate_effective_level(
            self.player.get_level('magic'),
            self.player.get_stat('magical_power')
        )

        physical_defense: int = self.monster.get_stat('physical_defense')
        magical_barrier: int = self.monster.get_stat('magical_barrier')

        self.player_max_hit = self._calculate_total_max_hit(
            physical_strength, physical_defense, magical_power, magical_barrier
        )

        # Monster max hit
        physical_strength: int = self.monster.get_stat('physical_strength')
        magical_power: int = self.monster.get_stat('magical_power')

        physical_defense: int = self._calculate_effective_level(
            self.player.get_level('defense'),
            self.player.get_stat('physical_defense')
        )
        magical_barrier: int = self._calculate_effective_level(
            self.player.get_level('defense'),
            self.player.get_stat('magical_barrier')
        )

        self.monster_max_hit = self._calculate_total_max_hit(
            physical_strength, physical_defense, magical_power, magical_barrier
        )

    def tick(self, tick_count: int) -> CombatResult | None:
        monster_speed: int = self.monster.attack_speed
        player_speed: int = self.player.equipment['weapon'].attack_speed

        player_attacks: bool = tick_count % player_speed == 0
        monster_attacks: bool = (tick_count - 1) % monster_speed == 0

        if not player_attacks and not monster_attacks:
            return None

        xp: dict = {}
        player_damage: int = 0
        monster_damage: int = 0

        xp_per_dmg: float = 2.

        if monster_attacks:
            player_damage = self.calculate_damage_to_player(
                self.player, self.monster
            )
            player_damage = min(player_damage, self.player.hitpoints)
            self.player.damage(player_damage)
            xp['defense'] = float(player_damage) * xp_per_dmg

        if player_attacks:
            monster_damage = self.calculate_damage_to_monster(
                self.player, self.monster
            )
            monster_damage = min(monster_damage, self.monster.hitpoints)
            self.monster.damage(monster_damage)
            xp['attack'] = float(monster_damage) * xp_per_dmg

        return CombatResult(
            player_damage=player_damage,
            monster_damage=monster_damage,
            xp=xp
        )

    def calculate_damage_to_monster(
        self,
        player: Player,
        monster: Monster,
    ) -> int:
        if rand() > self.player_hit_chance:
            return 0

        damage: int = randint(1, self.player_max_hit + 1)

        return damage

    def calculate_damage_to_player(
        self,
        player: Player,
        monster: Monster,
    ) -> int:
        if rand() > self.monster_hit_chance:
            return 0

        damage: int = randint(1, self.monster_max_hit + 1)

        return damage

    def _calculate_effective_level(
        self,
        skill_level: int,
        equipment_stat: int,
    ) -> int:
        effective_level: int = skill_level - 1
        effective_level += equipment_stat

        return effective_level

    def _calculate_hit_chance(self, accuracy: int, evasiveness: int) -> float:
        delta: float = float(accuracy - evasiveness)

        k: float = 0.1
        prob: float = 1. / (1. + exp(-k * delta))
        prob = min(0.99, prob)
        prob = max(0.01, prob)

        return prob

    def _calculate_max_hit(self, strength_qty: int, defense_qty: int) -> int:
        delta: float = float(strength_qty - defense_qty)

        k: float = 0.01
        factor: float = 1. / (1. + exp(-k * delta))

        max_hit: int = int(factor * float(strength_qty + 5)) * 5

        return max_hit

    def _calculate_total_max_hit(
        self,
        physical_strength,
        physical_defense,
        magical_power,
        magical_barrier,
    ) -> int:
        max_physical: int = self._calculate_max_hit(
            physical_strength, physical_defense
        )
        max_magic: int = self._calculate_max_hit(
            magical_power, magical_barrier
        )
        max_hit: int = max_physical + max_magic

        return max_hit
