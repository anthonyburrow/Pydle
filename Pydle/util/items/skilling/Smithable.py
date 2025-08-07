from ..Produceable import Produceable


class Smithable(Produceable):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
