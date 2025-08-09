from abc import abstractmethod

from .CommandBase import CommandBase
from .CommandRegistry import COMMAND_REGISTRY
from .CommandType import CommandType


class Operation(CommandBase):

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)

        COMMAND_REGISTRY.register(cls, CommandType.OPERATION)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @abstractmethod
    def execute(self) -> None:
        pass
