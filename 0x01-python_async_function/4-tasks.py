#!/usr/bin/env python3
"""module that that implements on top of wait_n function
but rather calling task_wait_n"""
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Create and execute a list of tasks using task_wait_random.

    Parameters:
    - n (int): The number of tasks to create.
    - max_delay (int): The maximum delay in seconds for wait_random.

    Returns:
    - List[float]: A list of float values representing the
    results of wait_random.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    return await asyncio.gather(*tasks)
