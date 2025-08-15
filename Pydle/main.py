import argparse

from .commands.CommandRegistry import COMMAND_REGISTRY
from .util.files import PLAYER_SAVE_FILE
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
    if args.new and PLAYER_SAVE_FILE.exists():
        print((
            'Are you sure you want to make a new character? '
            'This will delete your previous file. [y/N]'
        ))
        answer: str = ui.get_input().lower()

        if not answer or answer in ('n', 'no'):
            pass
        elif answer in ('y', 'yes'):
            PLAYER_SAVE_FILE.unlink()
        else:
            ui.print('Unknown response. Aborting character deletion.')

    player: Player = Player(save_file=str(PLAYER_SAVE_FILE))

    # Load command metadata
    COMMAND_REGISTRY.load_commands()

    # Setup game controller
    controller: Controller = Controller(player, ui)
    controller.loop()


if __name__ == '__main__':
    main()
