from Pydle.util.items.ItemInstance import ItemInstance
from Pydle.util.items.ItemParser import ITEM_PARSER
from Pydle.util.monsters.MonsterInstance import MonsterInstance
from Pydle.util.monsters.MonsterParser import MONSTER_PARSER
from Pydle.util.player.EquipmentSlot import EquipmentSlot
from Pydle.util.player.Player import Player
from Pydle.util.player.SkillType import SkillType
from Pydle.util.Result import Result
from Pydle.util.structures.CombatEngine import CombatEngine
from Pydle.util.ticks import Ticks

PLAYER_NAME: str = 'TestPlayer'

PLAYER_GEAR: dict[EquipmentSlot, str | None] = {
    EquipmentSlot.WEAPON: 'poor copper longsword',
    EquipmentSlot.OFFHAND: None,
    EquipmentSlot.HELM: 'poor copper helm',
    EquipmentSlot.BODY: 'poor copper chestplate',
    EquipmentSlot.LEGS: 'poor copper platelegs',
    EquipmentSlot.GLOVES: 'poor copper gauntlets',
    EquipmentSlot.BOOTS: 'poor copper boots',
}

PLAYER_SKILL_LEVELS: dict[SkillType, int] = {
    SkillType.HITPOINTS: 1,
    SkillType.STRENGTH: 1,
    SkillType.DEFENSE: 1,
    SkillType.MAGIC: 1,
    SkillType.BARRIER: 1,
    SkillType.ACCURACY: 1,
    SkillType.EVASIVENESS: 1,
}

MONSTER_NAME: str = 'goblin'


def _configure_player() -> Player:
    player: Player = Player(name=PLAYER_NAME)

    for skill_type, level in PLAYER_SKILL_LEVELS.items():
        player.set_level(skill_type, level)

    for equipment_slot, gear_name in PLAYER_GEAR.items():
        if gear_name is None:
            continue

        item: ItemInstance = ITEM_PARSER.get_instance(gear_name)
        player.give(item)

        equip_result: Result = player.equip(item)
        if not equip_result.success:
            raise ValueError(
                f'Could not equip "{gear_name}": {equip_result.msg}'
            )

    player.heal_full()
    return player


def _expected_damage_per_attack(
    hit_chance: float,
    max_hit_strength: int,
    max_hit_magical: int,
) -> float:
    avg_strength: float = 0
    avg_magical: float = 0

    if max_hit_strength:
        avg_strength = (max_hit_strength + 1) * 0.5

    if max_hit_magical:
        avg_magical = (max_hit_magical + 1) * 0.5

    return hit_chance * (avg_strength + avg_magical)


def _dps(expected_damage_per_attack: float, attack_speed_ticks: int) -> float:
    return expected_damage_per_attack / Ticks(attack_speed_ticks)


def _kills_per_hour(player_dps: float, monster_hitpoints: int) -> float:
    if player_dps <= 0.0 or monster_hitpoints <= 0:
        return 0.0

    time_per_kill_seconds = monster_hitpoints / player_dps
    return 3600.0 / time_per_kill_seconds


def print_combat_summary() -> None:
    player: Player = _configure_player()
    monster: MonsterInstance = MONSTER_PARSER.get_instance(MONSTER_NAME)

    engine: CombatEngine = CombatEngine(player, monster)

    player_max_hit: int = engine.player_total_max_hit
    monster_max_hit: int = engine.monster_total_max_hit

    player_weapon: ItemInstance | None = player.equipment[EquipmentSlot.WEAPON]
    player_attack_speed: int = (
        player_weapon.attack_speed if player_weapon else 3
    )
    monster_attack_speed: int = monster.attack_speed

    player_expected_damage = _expected_damage_per_attack(
        engine.player_hit_chance,
        engine.player_max_hit_strength,
        engine.player_max_hit_magical,
    )
    monster_expected_damage = _expected_damage_per_attack(
        engine.monster_hit_chance,
        engine.monster_max_hit_strength,
        engine.monster_max_hit_magical,
    )

    player_dps = _dps(player_expected_damage, player_attack_speed)
    monster_dps = _dps(monster_expected_damage, monster_attack_speed)
    kills_per_hour = _kills_per_hour(player_dps, monster.max_hitpoints)

    # --- Player stats ---
    print(f'=== Player: {player.name} ===')
    print('Skills:')
    for skill_type, level in PLAYER_SKILL_LEVELS.items():
        print(f'  {skill_type.name.title():<14}: {level}')
    print('Equipment stats:')
    for stat_key, value in player.stats.items():
        print(f'  {stat_key.replace("_", " ").title():<20}: {value}')
    print(f'  {"Attack speed":<20}: {player_attack_speed} ticks')

    print('')

    # --- Monster stats ---
    print(f'=== Monster: {monster.name.title()} ===')
    print(f'  {"Level":<20}: {monster.level}')
    print(f'  {"Hitpoints":<20}: {monster.max_hitpoints}')
    print(f'  {"Attack speed":<20}: {monster_attack_speed} ticks')
    for stat_key, value in monster.stats.items():
        print(f'  {stat_key.replace("_", " ").title():<20}: {value}')

    print('')

    # --- Combat results ---
    print('=== Combat Results ===')
    print(f'Player total max hit: {player_max_hit}')
    print(f'  Strength max hit: {engine.player_max_hit_strength}')
    print(f'  Magical max hit: {engine.player_max_hit_magical}')
    print(f'Monster total max hit: {monster_max_hit}')
    print(f'  Strength max hit: {engine.monster_max_hit_strength}')
    print(f'  Magical max hit: {engine.monster_max_hit_magical}')
    print(f'Player hit chance: {engine.player_hit_chance * 100.0:.2f}%')
    print(f'Monster hit chance: {engine.monster_hit_chance * 100.0:.2f}%')
    print(f'Player DPS: {player_dps:.3f}')
    print(f'Monster DPS: {monster_dps:.3f}')
    print(f'Kills per hour: {kills_per_hour:.2f}')


if __name__ == '__main__':
    print_combat_summary()
