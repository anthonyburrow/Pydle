from Pydle.commands.Command import Command
from Pydle.commands.operations import testing as testing_operation_module
from Pydle.util.items.ItemParser import ITEM_PARSER


class CaptureUI:
    def __init__(self):
        self.messages: list[str] = []

    def print(self, message: str):
        self.messages.append(message)


def test_setup_requires_argument(test_player):
    ui = CaptureUI()
    command = Command.parse('testing setup')

    operation = testing_operation_module.TestingOperation(test_player, ui, command)
    operation.execute()

    assert ui.messages
    assert ui.messages[-1] == 'A setup name is needed. Use `testing setup [name]`.'


def test_setup_unknown_name_prints_available(test_player):
    ui = CaptureUI()
    command = Command.parse('testing setup unknown')

    operation = testing_operation_module.TestingOperation(test_player, ui, command)
    operation.execute()

    assert ui.messages
    assert 'Unknown setup `unknown`.' in ui.messages[-1]
    assert 'skilling' in ui.messages[-1]


def test_setup_skilling_applies_and_prints_success(test_player):
    ui = CaptureUI()
    command = Command.parse('testing setup skilling')
    pickaxe = ITEM_PARSER.get_instance('poor copper pickaxe')

    assert not test_player.has(pickaxe)

    operation = testing_operation_module.TestingOperation(test_player, ui, command)
    operation.execute()

    assert test_player.has(pickaxe)
    assert ui.messages
    assert ui.messages[-1] == 'Applied testing setup `skilling`.'
