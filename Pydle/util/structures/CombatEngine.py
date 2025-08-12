from dataclasses import dataclass
from numpy import exp
from numpy.random import rand, randint

from ..monsters.Monster import Monster
from ..player.Player import Player
from ..player.SkillType import SkillType


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
        self.player_max_hit_strength: int = 1
        self.player_max_hit_magical: int = 1

        self.monster_hit_chance: float = 0.
        self.monster_max_hit: int = 1

        self.calculate_values()

    def calculate_values(self):
        # Player hit chance
        accuracy: int = self._calculate_effective_level(
            self.player.get_level(SkillType.ACCURACY),
            self.player.get_stat('accuracy')
        )

        evasiveness: int = self.monster.get_stat('evasiveness')

        self.player_hit_chance = self._calculate_hit_chance(
            accuracy, evasiveness
        )

        # Monster hit chance
        accuracy: int = self.monster.get_stat('accuracy')

        evasiveness: int = self._calculate_effective_level(
            self.player.get_level(SkillType.EVASIVENESS),
            self.player.get_stat('evasiveness')
        )

        self.monster_hit_chance = self._calculate_hit_chance(
            accuracy, evasiveness
        )

        # Player max hit
        physical_strength: int = self._calculate_effective_level(
            self.player.get_level(SkillType.STRENGTH),
            self.player.get_stat('physical_strength')
        )
        physical_defense: int = self.monster.get_stat('physical_defense')

        self.player_max_hit_strength = self._calculate_max_hit(
            physical_strength, physical_defense
        )

        magical_power: int = self._calculate_effective_level(
            self.player.get_level(SkillType.MAGIC),
            self.player.get_stat('magical_power')
        )
        magical_barrier: int = self.monster.get_stat('magical_barrier')

        self.player_max_hit_magical = self._calculate_max_hit(
            magical_power, magical_barrier
        )

        # Monster max hit
        physical_strength: int = self.monster.get_stat('physical_strength')
        physical_defense: int = self._calculate_effective_level(
            self.player.get_level(SkillType.DEFENSE),
            self.player.get_stat('physical_defense')
        )

        self.monster_max_hit_strength = self._calculate_max_hit(
            physical_strength, physical_defense
        )

        magical_power: int = self.monster.get_stat('magical_power')
        magical_barrier: int = self._calculate_effective_level(
            self.player.get_level(SkillType.BARRIER),
            self.player.get_stat('magical_barrier')
        )

        self.monster_max_hit_magical = self._calculate_max_hit(
            magical_power, magical_barrier
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

        xp_per_dmg: float = 0.5

        if monster_attacks:
            dmg_strength, dmg_magical = self._calculate_damage(
                self.monster_hit_chance,
                self.monster_max_hit_strength,
                self.monster_max_hit_magical,
            )
            player_damage = dmg_strength + dmg_magical
            player_damage = min(player_damage, self.player.hitpoints)
            self.player.damage(player_damage)

            xp_defense = int(float(dmg_strength) * xp_per_dmg)
            xp[SkillType.DEFENSE] = float(xp_defense)

            xp_barrier = int(float(dmg_magical) * xp_per_dmg)
            xp[SkillType.BARRIER] = float(xp_barrier)

            xp_evasiveness = float(monster_damage) * xp_per_dmg
            xp_evasiveness *= self.monster_hit_chance
            xp[SkillType.EVASIVENESS] = float(xp_evasiveness)

        if player_attacks:
            dmg_strength, dmg_magical = self._calculate_damage(
                self.player_hit_chance,
                self.player_max_hit_strength,
                self.player_max_hit_magical,
            )
            monster_damage = dmg_strength + dmg_magical
            monster_damage = min(monster_damage, self.monster.hitpoints)
            self.monster.damage(monster_damage)

            xp_strength = int(dmg_strength * xp_per_dmg)
            xp[SkillType.STRENGTH] = float(xp_strength)

            xp_magical = int(dmg_magical * xp_per_dmg)
            xp[SkillType.MAGIC] = float(xp_magical)

            xp_accuracy = monster_damage * xp_per_dmg
            xp_accuracy *= 1. - self.player_hit_chance
            xp[SkillType.ACCURACY] = float(xp_accuracy)

            xp_hitpoints = int(monster_damage * xp_per_dmg * 0.5)
            xp[SkillType.HITPOINTS] = float(xp_hitpoints)

        return CombatResult(
            player_damage=player_damage,
            monster_damage=monster_damage,
            xp=xp
        )

    def _calculate_damage(
            self,
            hit_chance: float,
            max_hit_strength: int,
            max_hit_magical: int,
        ) -> tuple[int]:
        if rand() > hit_chance:
            return 0, 0

        damage_strength: int = 0
        if max_hit_strength > 0:
            damage_strength = randint(1, max_hit_strength + 1)

        damage_magical: int = 0
        if max_hit_magical > 0:
            damage_magical = randint(1, max_hit_magical + 1)

        return damage_strength, damage_magical

    def _calculate_effective_level(
        self,
        skill_level: int,
        equipment_stat: int,
    ) -> int:
        max_level: float = 126.
        target_max_equipment: float = 200.

        skill_scaled: float = skill_level / max_level
        equip_scaled: float = equipment_stat / target_max_equipment

        effective_level: float = (skill_scaled * equip_scaled)**0.5
        effective_level *= max_level + target_max_equipment

        return int(effective_level)

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

        max_hit: int = int(factor * float(strength_qty)) * 5

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
