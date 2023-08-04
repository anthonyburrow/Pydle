import asyncio


seconds_per_tick = 0.6


async def Ticks(n_ticks):
    print(f' sleeping {n_ticks} ticks')
    await asyncio.sleep(n_ticks * seconds_per_tick)
