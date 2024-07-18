from pathlib import Path
import pickle

from OSRSsim.util.structures import Player, Controller


path_save: str = './profile'


def start():
    Path(path_save).mkdir(parents=True, exist_ok=True)

    # Setup/load player
    character_file: str = f'{path_save}/character.save'

    if Path(character_file).is_file():
        with open(character_file, 'rb') as file:
            player: Player = pickle.load(file)
        player.update()
    else:
        player: Player = Player(save_file=character_file)
        player.save()

    # Setup activity control manager
    controller: Controller = Controller(player)
    controller.loop()


if __name__ == '__main__':
    start()
