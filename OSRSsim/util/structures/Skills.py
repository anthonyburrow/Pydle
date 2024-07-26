from .Skill import Skill
from ..colors import color, skill_to_color


# { skill_key : (Formal name, Skill type) }
SKILLS = {
    # Gathering skills
    'mining': ('Mining', 'gathering'),
    'woodcutting': ('Woodcutting', 'gathering'),
    'foraging': ('Foraging', 'gathering'),
    'fishing': ('Fishing', 'gathering'),
}


class Skills:

    def __init__(self):
        self._skills: dict = {}

    def get_skill(self, skill_key: str) -> Skill:
        return self._skills[skill_key]

    def get_skills(self) -> dict:
        return {skill_key: self.get_skill(skill_key) for skill_key in SKILLS}

    def get_skills_XP(self) -> dict:
        return {skill_key: self.get_skill(skill_key).XP for skill_key in SKILLS}

    def add_XP(self, skill_key: str, XP: float):
        return self.get_skill(skill_key).add_XP(XP)

    def set_XP(self, skill_key: str, XP: float):
        return self.get_skill(skill_key).set_XP(XP)

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

            skill_XP = skills_dict[skill_key]
            self._skills[skill_key] = Skill(*skill_info, XP=skill_XP)

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
            skill_line: str = f'{name} | Lvl {skill.level:<2} ({skill.XP:,.0f} EXP)'
            msg.append(skill_line)

        msg = '\n'.join(msg)

        return msg
