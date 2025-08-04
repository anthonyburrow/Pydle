from colorama import Fore, Style


BLACK = Fore.BLACK
RED = Fore.RED
GREEN = Fore.GREEN
YELLOW = Fore.YELLOW
BLUE = Fore.BLUE
MAGENTA = Fore.MAGENTA
CYAN = Fore.CYAN
WHITE = Fore.WHITE
END = Style.RESET_ALL


def color(text: str, color: str, justify: int = 0, just_type: str = 'right'):
    out_text = f'{color}{text}{END}'

    if not justify:
        return out_text

    just_amount = justify + len(color) + len(END)

    if just_type == 'right':
        out_text = f'{out_text:>{just_amount}}'
    elif just_type == 'left':
        out_text = f'{out_text:<{just_amount}}'

    return out_text


# THEME:
color_theme = {
    # UI elements
    'UI_1': MAGENTA,
    # Player
    'player': CYAN,
    # Items
    'tools': MAGENTA,
    'equipment': MAGENTA,
    'quality_poor': RED,
    'quality_good': MAGENTA,
    'quality_master': CYAN,
    # Skills
    'skill_gathering': GREEN,
    'skill_artisan': RED,
    'skill_combat': CYAN,
    'skill_support': MAGENTA,
    'skill_lvl99': YELLOW,
    # Monsters
    'monster_basic': MAGENTA,
    'monster_superior': RED,
    'monster_boss': RED,
}
