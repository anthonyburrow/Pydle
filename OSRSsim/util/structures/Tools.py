from . import Player
from ..colors import color, COLOR_TOOLS
from ...lib.data.skilling import mining, woodcutting, foraging


tool_types = {
    'pickaxe': mining.pickaxes,
    'axe': woodcutting.axes,
    'secateurs': foraging.secateurs,
}


class Tools:

    def __init__(self, player: Player):
        self._player = player
        self._tools = {tool: None for tool in tool_types}

    def add(self, tool: str) -> dict:
        if not self._player.has(tool):
            msg = f'{self._player} does not have a {tool}.'
            return {
                'success': False,
                'msg': msg,
            }

        for tool_type, tool_dict in tool_types.items():
            if tool not in tool_dict:
                continue

            old_tool = self._tools[tool_type]
            if old_tool is not None:
                self._player.give(old_tool)

            self._player.remove(tool, quantity=1)
            self._tools[tool_type] = tool

            msg = f"{tool.capitalize()} was added to {self._player}'s toolbelt."
            return {
                'success': True,
                'msg': msg,
            }

        msg = f"{tool.capitalize()} cannot be placed in {self._player}'s toolbelt."
        return {
            'success': False,
            'msg': msg,
        }

    def remove(self, tool_type: str) -> dict:
        if tool_type not in self._tools or self._tools[tool_type] is None:
            msg = f'{self._player} has no {tool_type} equipped.'
            return {
                'success': False,
                'msg': msg,
            }

        tool = self._tools[tool_type]
        self._tools[tool_type] = None
        self._player.give(tool)

        msg = f"{tool.capitalize()} was removed {self._player}'s toolbelt."
        return {
            'success': True,
            'msg': msg,
        }

    def get_tool(self, tool_type: str) -> str:
        return self._tools[tool_type]

    def __str__(self) -> str:
        msg_out: list = []
        just_amount: int = max([len(t) for t in tool_types])
        for tool_type, tool in self._tools.items():
            name = color(tool_type.capitalize(), COLOR_TOOLS, justify=just_amount)
            _tool = tool.capitalize() if tool is not None else '---'
            tool_line = f'  {name} | {_tool}'
            msg_out.append(tool_line)

        msg = '\n' + '\n'.join(msg_out) + '\n'

        return msg
