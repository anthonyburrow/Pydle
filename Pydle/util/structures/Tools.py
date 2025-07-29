from . import Player, Tool
from ..colors import color
from ..Result import Result
from ...lib.skilling import mining, woodcutting, foraging, fishing


TOOLS = {
    'pickaxe': mining.PICKAXES,
    'axe': woodcutting.AXES,
    'secateurs': foraging.SECATEURS,
    'fishing rod': fishing.FISHING_RODS,
}


class Tools(dict):

    def __init__(self, player: Player, tools_dict: dict = None):
        self._player: Player = player

        tools_dict = tools_dict or {}

        for tool_key, tools_lib in TOOLS.items():
            tool_name: str = tools_dict.get(tool_key, '')
            self[tool_key] = tools_lib.get(tool_name, '')

    def equip(self, tool: str) -> Result:
        if not self._player.has(tool):
            return Result(
                success=False,
                msg=f'{self._player} does not have a {tool}.',
            )

        for tool_type, tool_dict in TOOLS.items():
            if tool not in tool_dict:
                continue

            old_tool = self.get_tool(tool_type)
            if old_tool:
                self._player.give(old_tool.name)

            self._player.remove(tool, quantity=1)
            tool_obj = tool_dict[tool]
            self[tool_type] = tool_obj

            return Result(
                success=True,
                msg=f"{tool_obj} was equipped to {self._player}'s toolbelt.",
            )

        return Result(
            success=False,
            msg=f"{tool.capitalize()} cannot be placed in {self._player}'s toolbelt.",
        )

    def unequip(self, tool_type: str) -> Result:
        if tool_type not in self:
            return Result(
                success=False,
                msg=f'{tool_type.capitalize()} is not a valid type of tool (axe, pickaxe, etc.).',
            )

        old_tool: Tool = self.get_tool(tool_type)
        if not old_tool:
            return Result(
                success=False,
                msg=f'{self._player} has no {tool_type} equipped.',
            )

        self[tool_type] = ''
        self._player.give(old_tool.name)

        return Result(
            success=True,
            msg=f"{old_tool} was unequipped from {self._player}'s toolbelt.",
        )

    def get_tool(self, tool_key: str) -> Tool:
        return self[tool_key]

    def get_tools(self) -> dict:
        return {
            tool_key: self.get_tool(tool_key)
            for tool_key in TOOLS
        }

    def to_dict(self) -> dict:
        tool_names: dict = {}

        for tool_key in TOOLS:
            tool: Tool = self.get_tool(tool_key)
            tool_names[tool_key] = tool.name if tool else ''

        return tool_names

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
            tool_str = tool or '---'
            tool_line = f'{name} | {tool_str}'
            msg.append(tool_line)

        msg = '\n'.join(msg)

        return msg
