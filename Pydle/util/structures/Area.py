from ..ticks import Ticks


class Area:

    def __init__(
        self,
        name: str,
        coordinates: tuple[int],
        requirements: list[callable] = None,
        # Combat
        monsters: set[str] = None,
        # Gatherables
        fish: set[str] = None,
        herbs: set[str] = None,
        logs: set[str] = None,
        ores: set[str] = None,
    ):
        self.name: str = name
        self.coordinates: tuple[int] = coordinates
        self.requirements: list = requirements or []
        # Combat
        self.monsters: set[str] = monsters or set()
        # Gatherables
        self.fish: set[str] = fish or set()
        self.herbs: set[str] = herbs or set()
        self.logs: set[str] = logs or set()
        self.ores: set[str] = ores or set()

    def travel_ticks(self, current_coordinates: tuple[int]) -> int:
        x0, y0 = current_coordinates
        x, y = self.coordinates

        time_sec = 60. * ((x - x0)**2 + (y - y0)**2)**0.5
        time_ticks = int(time_sec / Ticks()) + 1

        return time_ticks

    def contains_monster(self, monster: str) -> bool:
        return monster in self.monsters

    def contains_fish(self, fish: str) -> bool:
        return fish in self.fish

    def contains_herb(self, herb: str) -> bool:
        return herb in self.herbs

    def contains_log(self, log: str) -> bool:
        return log in self.logs

    def contains_monster(self, monster: str) -> bool:
        return monster in self.monsters

    def __str__(self) -> str:
        return self.name
