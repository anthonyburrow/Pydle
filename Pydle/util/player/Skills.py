from .Skill import Skill
from .SkillType import SkillType
from ..colors import color, color_theme
from ..visuals import centered_title


SKILLS = {
    SkillType.HITPOINTS: 'combat',
    SkillType.STRENGTH: 'combat',
    SkillType.DEFENSE: 'combat',
    SkillType.MAGIC: 'combat',
    SkillType.BARRIER: 'combat',
    SkillType.ACCURACY: 'combat',
    SkillType.EVASIVENESS: 'combat',
    SkillType.FISHING: 'gathering',
    SkillType.FORAGING: 'gathering',
    SkillType.MINING: 'gathering',
    SkillType.WOODCUTTING: 'gathering',
    SkillType.COOKING: 'artisan',
    SkillType.CRAFTING: 'artisan',
    SkillType.HERBLORE: 'artisan',
    SkillType.SMITHING: 'artisan',
}

class Skills(dict):

    def __init__(self, skills_dict: dict[SkillType, float] = None):
        skills_dict = skills_dict or {}
        self.load_from_dict(skills_dict)

    def add_xp(self, skill_type: SkillType, xp: float):
        return self[skill_type].add_xp(xp)

    def set_xp(self, skill_type: SkillType, xp: float):
        return self[skill_type].set_xp(xp)

    def set_level(self, skill_type: SkillType, level: int):
        return self[skill_type].set_level(level)

    def get_level(self, skill_type: SkillType) -> int:
        return self[skill_type].level

    def to_dict(self) -> dict[str, float]:
        return {
            skill_key.name: float(self[skill_key].xp)
            for skill_key in SKILLS
        }

    def load_from_dict(self, skills_dict: dict[SkillType, float]) -> None:
        for skill_type, skill_category in SKILLS.items():
            xp: float = skills_dict.get(skill_type, 0.)
            self[skill_type] = Skill(skill_type, skill_category, xp=xp)

    def __str__(self) -> str:
        msg: list = []

        max_skill_length: int = max([len(x.name) for x in self])
        max_level_length: int = max([len(str(x.level)) for x in self.values()])
        max_exp_length: int = max([len(f'{x.xp:,.0f}') for x in self.values()])
        total_length = max_skill_length + max_level_length + max_exp_length + 14

        msg.append(centered_title('SKILLS', total_length))

        for skill_key in SKILLS:
            skill: Skill = self[skill_key]
            name: str = color(
                skill.skill_type,
                color_theme[f'skill_{skill.skill_category}'],
                justify=max_skill_length,
            )
            exp_str = f'{skill.xp:,.0f}'
            skill_line: str = f'{name} | Lvl {skill.level:>{max_level_length}} | {exp_str:>{max_exp_length}} Exp'
            msg.append(skill_line)

        msg = '\n'.join(msg)

        return msg

    def __setitem__(self, key, value):
        if key not in SKILLS:
            raise KeyError(f'Invalid skill key: "{key}"')
        super().__setitem__(key, value)
