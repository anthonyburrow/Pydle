import asyncio

from .Activity import Activity


class ActivityManager:

    def __init__(self):
        self.active_tasks = {}

    async def add(self, activity: Activity) -> None:
        pass
