#!/usr/bin/env python3
"""module that uses the wait_random async function and futher
implement more functionality
"""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronous routine that spawns wait_random n
    times with the specified max_delay.

    Parameters:
    - n (int): The number of times to spawn wait_random.
    - max_delay (int): The maximum delay in seconds
    for each wait_random call.

    Returns:
    - List[float]: A list of delays in ascending order
    without using sort().
    """
    delays = [wait_random(max_delay) for _ in range(n)]
    gathered_delays: List[float] = await asyncio.gather(*delays)
    return sorted(gathered_delays)
