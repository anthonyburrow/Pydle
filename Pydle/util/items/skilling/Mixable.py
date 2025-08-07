from ..Produceable import Produceable


class Mixable(Produceable):

    def __init__(self, n_doses: int = 1, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.n_doses: int = n_doses
