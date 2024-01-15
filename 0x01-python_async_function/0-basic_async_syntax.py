#!/usr/bin/env python3
"""module that implements a basic async/await function"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronously waits for a random delay.

    This coroutine waits for a random amount of time between
    0 and max_delay seconds, then returns the actual 
    delay time.

    Parameters:
    - max_delay (int): The maximum delay time in seconds.
    Default is 10.

    Returns:
    - float: The actual delay time in seconds.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay