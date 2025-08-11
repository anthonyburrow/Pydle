import argparse
from pathlib import Path
from platformdirs import user_data_dir

from .commands.CommandRegistry import COMMAND_REGISTRY
from .util.player.Player import Player
from .util.structures.Controller import Controller
from .util.structures.UserInterface import UserInterface


APP_NAME = 'Pydle'


def main():
    # Get any arguments to script
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--new',
        action='store_true',
        help='Delete save file and start new character'
    )

    args = parser.parse_args()

    # Setup UI
    ui: UserInterface = UserInterface()

    # Setup/load player
    path_save: Path = Path(user_data_dir(APP_NAME))
    path_save.mkdir(parents=True, exist_ok=True)

    if args.new:
        ui.print((
            'Are you sure you want to make a new character? [Y/n]'
            'This will delete your previous file.'
        ))
        answer: str = ui.get_input.lower()

        if answer in ('y', 'yes'):
            #delete
            pass
        elif answer in ('n', 'no'):
            pass
        else:
            ui.print('Unknown response')

    character_file: str = str(path_save / 'player.json')
    player: Player = Player(save_file=character_file)

    # Load command metadata
    COMMAND_REGISTRY.load_commands()

    # Setup game controller
    controller: Controller = Controller(player, ui)
    controller.loop()


if __name__ == '__main__':
    main()
