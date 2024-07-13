from pathlib import Path
import pickle

from OSRSsim.util.structures import Player
from OSRSsim.util import Controller


path_save = './profile'


def start():
    Path(path_save).mkdir(parents=True, exist_ok=True)

    # Setup/load player
    character_file = f'{path_save}/character.save'

    if Path(character_file).is_file():
        with open(character_file, 'rb') as file:
            player = pickle.load(file)
    else:
        player = Player(save_file=character_file)
        player.save()

    # Setup activity control manager
    controller = Controller(player)
    controller.loop()


if __name__ == '__main__':
    start()
