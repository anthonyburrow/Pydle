from .Skill import Skill
from ..colors import color, skill_to_color


# { skill_key : (Formal name, Skill type) }
SKILLS = {
    # Combat skills
    'hitpoints': ('Hitpoints', 'combat'),
    'strength': ('Strength', 'combat'),
    'defense': ('Defense', 'combat'),
    'magic': ('Magic', 'combat'),
    'barrier': ('Barrier', 'combat'),
    'accuracy': ('Accuracy', 'combat'),
    'evasiveness': ('Evasiveness', 'combat'),
    # Gathering skills
    'fishing': ('Fishing', 'gathering'),
    'foraging': ('Foraging', 'gathering'),
    'mining': ('Mining', 'gathering'),
    'woodcutting': ('Woodcutting', 'gathering'),
    # Artisan skills
    'cooking': ('Cooking', 'artisan'),
    'crafting': ('Crafting', 'artisan'),
    'herblore': ('Herblore', 'artisan'),
    'smithing': ('Smithing', 'artisan'),
}


class Skills(dict):

    def __init__(self, skills_dict: dict = None):
        skills_dict = skills_dict or {}

        for skill_key, skill_info in SKILLS.items():
            xp: float = skills_dict.get(skill_key, 0.)
            self[skill_key] = Skill(*skill_info, xp=xp)

    def get_skill(self, skill_key: str) -> Skill:
        return self[skill_key]

    def get_skills(self) -> dict:
        return {skill_key: self.get_skill(skill_key) for skill_key in SKILLS}

    def add_xp(self, skill_key: str, xp: float):
        return self.get_skill(skill_key).add_xp(xp)

    def set_xp(self, skill_key: str, xp: float):
        return self.get_skill(skill_key).set_xp(xp)

    def set_level(self, skill_key: str, level: int):
        return self.get_skill(skill_key).set_level(level)

    def get_level(self, skill_key: str) -> int:
        return self.get_skill(skill_key).level

    def to_dict(self) -> dict:
        return {
            skill_key: float(self.get_skill(skill_key).xp)
            for skill_key in SKILLS
        }

    def __str__(self) -> str:
        msg: list = []
        just_amount: int = max([len(s) for s in SKILLS])
        for skill_key in SKILLS:
            skill: Skill = self.get_skill(skill_key)
            name: str = color(
                skill.name,
                skill_to_color(skill.skill_type),
                justify=just_amount,
            )
            skill_line: str = f'{name} | Lvl {skill.level:<2} ({skill.xp:,.0f} Exp)'
            msg.append(skill_line)

        msg = '\n'.join(msg)

        return msg
