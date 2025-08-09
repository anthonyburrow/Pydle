from ...Activity import (
    Activity,
    ActivitySetupResult,
    ActivityMsgType,
    ActivityTickResult
)
from ....util.structures.Area import Area
from ....lib.areas import AREAS


class TravelingActivity(Activity):

    name: str = 'travel'
    help_info: str = 'Begin traveling to a different area.'

    def __init__(self, *args):
        super().__init__(*args)

        if self.argument in AREAS:
            self.area: Area = AREAS[self.command.argument]
            self.area_key: str = self.command.argument
        else:
            self.area: Area = None

        self.description: str = 'traveling'

        if self.area is not None:
            current_area = AREAS[self.player.area]
            self.travel_ticks = self.area.travel_ticks(
                current_area.coordinates
            )

    @classmethod
    def usage(cls) -> str:
        msg: list[str] = []

        msg.append('Use cases:')
        msg.append('- travel [area]')

        msg.append('')

        msg.append('Available areas:')
        for area in AREAS:
            name = str(area).capitalize()
            msg.append(f'- {name}')

        return '\n'.join(msg)

    def setup_inherited(self) -> ActivitySetupResult:
        if self.area is None:
            return ActivitySetupResult(
                success=False,
                msg='A valid area was not given.'
            )

        if self.area_key == self.player.area:
            return ActivitySetupResult(
                success=False,
                msg=f'{self.player} is already at {self.area}.'
            )

        for req in self.area.requirements:
            if req(self.player):
                continue

            return ActivitySetupResult(
                success=False,
                msg=f'{self.player} is missing requirements to travel to {self.area}.'
            )

        return ActivitySetupResult(success=True)

    def update_inherited(self) -> ActivityTickResult:
        '''Processing during each tick.'''
        if self.tick_count < self.travel_ticks:
            return ActivityTickResult(
                msg=self.standby_text,
                msg_type=ActivityMsgType.WAITING,
            )

        self.player.set_area(self.area_key)

        return ActivityTickResult(
            msg=f'{self.player} arrived at {self.area}.',
            exit=True,
        )

    def finish_inherited(self):
        pass

    @property
    def startup_text(self) -> str:
        return f'{self.player} is now traveling to {self.area}.'

    @property
    def standby_text(self) -> str:
        return 'Traveling...'

    @property
    def finish_text(self) -> str:
        return ''
