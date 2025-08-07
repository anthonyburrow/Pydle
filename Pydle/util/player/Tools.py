from .Player import Player
from .ToolSlot import ToolSlot
from ..Result import Result
from ..visuals import centered_title
from ..items.ItemInstance import ItemInstance
from ..items.Tool import Tool


class Tools(dict):

    def __init__(self, player: Player, tools_dict: dict | None = None):
        self._player: Player = player

        tools_dict = tools_dict or {}
        self.load_from_dict(tools_dict)

    def equip(self, item_instance: ItemInstance) -> Result:
        if not self._player.has(item_instance):
            return Result(
                success=False,
                msg=f'{self._player} does not have a {item_instance}.',
            )

        tool_slot: ToolSlot = item_instance.tool_slot

        previous_instance: Tool | None = self.get(tool_slot)
        if previous_instance:
            self._player.give(previous_instance)

        self._player.remove(item_instance)
        self[tool_slot] = item_instance

        return Result(
            success=True,
            msg=f"{item_instance} was equipped to {self._player}'s toolbelt."
        )

    def unequip(self, item_instance: ItemInstance) -> Result:
        tool_slot: ToolSlot = item_instance.tool_slot

        previous_instance: Tool | None = self.get(tool_slot)
        if not previous_instance or previous_instance != item_instance:
            return Result(
                success=False,
                msg=f'{self._player} does not have a {item_instance} equipped.',
            )

        self[tool_slot] = None
        self._player.give(item_instance)

        return Result(
            success=True,
            msg=f"{previous_instance} was unequipped from {self._player}'s toolbelt.",
        )

    def to_dict(self) -> dict[str, dict | None]:
        tool_dict: dict[str, dict | None] = {}

        for tool_slot, item_instance in self.items():
            if not item_instance:
                tool_dict[tool_slot.name] = None
                continue
            tool_dict[tool_slot.name] = item_instance.to_dict()

        return tool_dict

    def load_from_dict(self, tools_dict: dict) -> None:
        for tool_slot in ToolSlot:
            instance_dict: dict | None = tools_dict.get(tool_slot.name)

            if instance_dict is None:
                self[tool_slot] = None
                continue

            tool_instance: Tool = Tool.from_dict(instance_dict)
            self[tool_slot] = tool_instance

        return self

    def __str__(self) -> str:
        msg: list = []

        max_type_length: int = max([len(str(x)) for x in ToolSlot])
        max_tool_length: int = 0
        for item_instance in self.values():
            if item_instance is None:
                length = 3
            else:
                length = len(item_instance.name)
            if length > max_tool_length:
                max_tool_length = length
        total_length = max_type_length + max_tool_length + 3

        msg.append(centered_title('TOOLS', total_length))

        for tool_slot, item_instance in self.items():
            tool_str = item_instance or '---'
            msg.append(f'{tool_slot:>{max_type_length}} | {tool_str}')

        msg = '\n'.join(msg)

        return msg

    def __setitem__(self, key, value):
        if key not in ToolSlot:
            raise KeyError(f'Invalid ToolSlot key: "{key}"')
        super().__setitem__(key, value)
