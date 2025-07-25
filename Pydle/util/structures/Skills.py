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


class Skills:

    def __init__(self):
        self._skills: dict = {}

    def get_skill(self, skill_key: str) -> Skill:
        return self._skills[skill_key]

    def get_skills(self) -> dict:
        return {skill_key: self.get_skill(skill_key) for skill_key in SKILLS}

    def get_skills_xp(self) -> dict:
        return {skill_key: self.get_skill(skill_key).xp for skill_key in SKILLS}

    def add_xp(self, skill_key: str, xp: float):
        return self.get_skill(skill_key).add_xp(xp)

    def set_xp(self, skill_key: str, xp: float):
        return self.get_skill(skill_key).set_xp(xp)

    def set_level(self, skill_key: str, level: int):
        return self.get_skill(skill_key).set_level(level)

    def get_level(self, skill_key: str) -> int:
        return self.get_skill(skill_key).level

    def load_skills(self, skills_dict: dict = None):
        for skill_key, skill_info in SKILLS.items():
            if skills_dict is None:
                self._skills[skill_key] = Skill(*skill_info)
                continue

            if skill_key not in skills_dict:
                self._skills[skill_key] = Skill(*skill_info)
                continue

            skill_xp = skills_dict[skill_key]
            self._skills[skill_key] = Skill(*skill_info, xp=skill_xp)

    @property
    def skills(self) -> dict:
        return self._skills

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
