from ....util.structures.Produceable import Produceable


class Craftable(Produceable):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
