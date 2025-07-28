from . import Player, Tool
from ..colors import color
from ...lib.skilling import mining, woodcutting, foraging, fishing


TOOLS = {
    'pickaxe': mining.PICKAXES,
    'axe': woodcutting.AXES,
    'secateurs': foraging.SECATEURS,
    'fishing rod': fishing.FISHING_RODS,
}


class Tools(dict):

    def __init__(self, player: Player):
        self._player: Player = player

    def equip(self, tool: str) -> dict:
        if not self._player.has(tool):
            msg = f'{self._player} does not have a {tool}.'
            return {
                'success': False,
                'msg': msg,
            }

        for tool_type, tool_dict in TOOLS.items():
            if tool not in tool_dict:
                continue

            old_tool = self.get_tool(tool_type)
            if old_tool is not None:
                self._player.give(old_tool.name)

            self._player.remove(tool, quantity=1)
            tool_obj = tool_dict[tool]
            self[tool_type] = tool_obj

            msg = f"{tool_obj} was equipped to {self._player}'s toolbelt."
            return {
                'success': True,
                'msg': msg,
            }

        msg = f"{tool.capitalize()} cannot be placed in {self._player}'s toolbelt."
        return {
            'success': False,
            'msg': msg,
        }

    def unequip(self, tool_type: str) -> dict:
        old_tool: Tool = self.get_tool(tool_type)
        if old_tool is None:
            msg: str = f'{self._player} has no {tool_type} equipped.'
            return {
                'success': False,
                'msg': msg,
            }

        self[tool_type] = None
        self._player.give(old_tool.name)

        msg: str = f"{old_tool} was unequipped from {self._player}'s toolbelt."
        return {
            'success': True,
            'msg': msg,
        }

    def get_tool(self, tool_key: str) -> Tool:
        return self[tool_key]

    def get_tools(self) -> dict:
        return {tool_key: self.get_tool(tool_key) for tool_key in TOOLS}

    def get_tools_names(self) -> dict:
        tool_names = {}
        for tool_key in TOOLS:
            tool = self.get_tool(tool_key)
            if tool is None:
                tool_names[tool_key] = ''
            else:
                tool_names[tool_key] = tool.name

        return tool_names

    def load_tools(self, tools_dict: dict = None):
        for tool_key, tools_lib in TOOLS.items():
            # Basically only procs if new player
            if tools_dict is None:
                self[tool_key] = None
                continue

            # Occurs when there's additions to TOOLS
            if tool_key not in tools_dict:
                self[tool_key] = None
                continue

            tool_name = tools_dict[tool_key]

            if tool_name is None or not tool_name:
                self[tool_key] = None
                continue

            self[tool_key] = tools_lib[tool_name]

    def __str__(self) -> str:
        msg: list = []
        just_amount: int = max([len(t) for t in TOOLS])
        for tool_key in TOOLS:
            tool: Tool = self.get_tool(tool_key)
            name = color(
                tool_key.capitalize(),
                '',
                justify=just_amount
            )
            tool_str = tool if tool is not None else '---'
            tool_line = f'{name} | {tool_str}'
            msg.append(tool_line)

        msg = '\n'.join(msg)

        return msg
