#!/usr/bin/env python3
"""module that calls an async 4x and measures total runtime"""
import asyncio

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Measure the runtime of the async_comprehension coroutine
    executed four times in parallel using asyncio.gather.

    Returns:
        float: Total runtime in seconds.
    Usage:
    ```python
    total_runtime = await measure_runtime()
    print(f"Total runtime: {total_runtime} seconds")
    ```
    """
    start = asyncio.get_event_loop().time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end = asyncio.get_event_loop().time()
    return end - start
