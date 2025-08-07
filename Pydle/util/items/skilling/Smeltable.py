from ..Produceable import Produceable


class Smeltable(Produceable):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
