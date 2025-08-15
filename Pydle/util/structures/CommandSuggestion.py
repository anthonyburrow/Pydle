from prompt_toolkit.auto_suggest import AutoSuggest, Suggestion

from ..items.ItemParser import ITEM_PARSER
from ..monsters.MonsterParser import MONSTER_PARSER
from ...commands.CommandRegistry import COMMAND_REGISTRY
from ...lib.areas.areas import AREAS


class CommandSuggestion(AutoSuggest):

    def __init__(self):
        self.commands: list[str] = []
        self.commands.extend(a.name for a in COMMAND_REGISTRY.activities.values())
        self.commands.extend(o.name for o in COMMAND_REGISTRY.operations.values())

        self.monster_commands: set[str] = {'kill'}
        self.area_commands: set[str] = {'area', 'travel'}

    def get_suggestion(self, buffer, document) -> Suggestion | None:
        text: str = document.text_before_cursor
        tokens: list[str] = text.split()

        if not tokens:
            return None

        if len(tokens) == 1:
            for command in self.commands:
                if not command.startswith(text):
                    continue
                remainder: str = command[len(tokens[0]):]
                if remainder:
                    return Suggestion(remainder)

        command: str = tokens[0]
        len_command: int = len(command)

        if len(tokens) >= 2:
            argument: str = text[len_command:].lstrip()

            if command in self.monster_commands:
                for monster in MONSTER_PARSER.name_map:
                    if not monster.startswith(argument):
                        continue
                    remainder: str = monster[len(argument):]
                    if remainder:
                        return Suggestion(remainder)
            elif command in self.area_commands:
                for area in AREAS:
                    if not area.startswith(argument):
                        continue
                    remainder: str = area[len(argument):]
                    if remainder:
                        return Suggestion(remainder)
            else:
                for item in ITEM_PARSER.name_map:
                    if not item.startswith(argument):
                        continue
                    remainder: str = item[len(argument):]
                    if remainder:
                        return Suggestion(remainder)

        return None