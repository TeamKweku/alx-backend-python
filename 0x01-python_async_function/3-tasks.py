#!/usr/bin/env python3
"""a module that implement a regular function that returns
asyncio.Task
"""
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Creates an asyncio.Task that runs wait_random with
    the specified max_delay.

    Parameters:
    - max_delay (int): The maximum delay for wait_random.

    Returns:
    - asyncio.Task: A task that will run wait_random.
    """
    return asyncio.create_task(wait_random(max_delay))