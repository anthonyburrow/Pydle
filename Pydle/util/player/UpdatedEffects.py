from ..colors import color


class UpdatedEffects(dict):

    def __init__(self, effects_dict: dict[str, int] | None = None):
        self.load_from_dict(effects_dict or {})

    def add_effect(self, effect_key: str, effect_ticks: int):
        self[effect_key] = effect_ticks

    def remove_effect(self, effect_key: str):
        if effect_key not in self:
            return
        self.pop(effect_key)

    def has_effect(self, effect_key: str) -> bool:
        return effect_key in self

    def update_effects(self) -> None:
        keys_to_remove = []
        for effect_key, effect_ticks in self.items():
            self[effect_key] = effect_ticks - 1
            if self[effect_key] <= 0:
                keys_to_remove.append(effect_key)

        for effect_key in keys_to_remove:
            self.remove_effect(effect_key)

    def to_dict(self) -> dict[str, int]:
        return dict(self)

    def load_from_dict(self, effects_dict: dict[str, int]) -> None:
        for effect_key, effect_ticks in effects_dict.items():
            self[effect_key] = effect_ticks

    def __str__(self) -> str:
        if not self:
            return 'No ongoing effects.'

        msg: list = []
        just_amount: int = max([len(s) for s in self])
        for effect_key, effect_ticks in self.items():
            name = color(
                effect_key.capitalize(),
                '',
                justify=just_amount
            )
            msg.append(f'{name} : {effect_ticks}')

        return '\n'.join(msg)
