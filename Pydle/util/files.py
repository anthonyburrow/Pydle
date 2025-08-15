from pathlib import Path
from platformdirs import user_data_dir


APP_NAME = 'Pydle'


USER_DIR: Path = Path(user_data_dir(APP_NAME))
USER_DIR.mkdir(parents=True, exist_ok=True)

PLAYER_SAVE_FILE: Path = USER_DIR / 'player.json'
