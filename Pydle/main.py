from platformdirs import user_data_dir
from pathlib import Path

from .util.player.Player import Player
from .util.structures.Controller import Controller
from .util.structures.UserInterface import UserInterface


APP_NAME = 'Pydle'


def main():
    # Setup/load player
    path_save: Path = Path(user_data_dir(APP_NAME))
    path_save.mkdir(parents=True, exist_ok=True)

    character_file: str = str(path_save / 'player.json')
    player: Player = Player(save_file=character_file)

    # Setup UI
    ui: UserInterface = UserInterface()

    # Setup game controller
    controller: Controller = Controller(player, ui)
    controller.loop()


if __name__ == '__main__':
    main()
