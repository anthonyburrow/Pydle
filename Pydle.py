from pathlib import Path

from Pydle.util.structures.Player import Player
from Pydle.util.structures.Controller import Controller


path_save: str = './profile'


def start():
    Path(path_save).mkdir(parents=True, exist_ok=True)

    # Setup/load player
    character_file: str = f'{path_save}/character.save'
    player: Player = Player(save_file=character_file)

    # Setup activity control manager
    controller: Controller = Controller(player)
    controller.loop()


if __name__ == '__main__':
    start()
