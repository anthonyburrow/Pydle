from platformdirs import user_data_dir
from pathlib import Path

from .util.structures.Player import Player
from .util.structures.Controller import Controller


APP_NAME = 'Pydle'


def main():
    path_save: Path = Path(user_data_dir(APP_NAME))
    path_save.mkdir(parents=True, exist_ok=True)

    # Setup/load player
    character_file: str = str(path_save / 'player.json')
    player: Player = Player(save_file=character_file)

    # Setup activity control manager
    controller: Controller = Controller(player)
    controller.loop()


if __name__ == '__main__':
    main()
