from abc import ABC

from .Quality import Quality


class Item(ABC):
    def __init__(self, item_id: str, name: str, supported_qualities=None):
        self.item_id: str = item_id
        self.name: str = name
        self.supported_qualities: list[Quality] = supported_qualities or []

    def __repr__(self):
        return f'<Item id={self.item_id}, name={self.name}>'

    def __str__(self):
        return self.name.title()
