from OSRSsim.util.structures import Player
from OSRSsim.util import Controller


def start():
    # Setup/load player
    player = Player()

    # Setup activity control manager
    controller = Controller(player)
    controller.loop()


if __name__ == '__main__':
    start()
