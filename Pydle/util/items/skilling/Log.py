from ....util.structures.Gatherable import Gatherable


class Log(Gatherable):

    def __init__(self, ticks_per_fire, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.ticks_per_fire: int = ticks_per_fire
