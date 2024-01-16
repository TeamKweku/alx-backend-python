#!/usr/bin/env python3
"""a module that implements a coroutine that runs 10x"""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[int, None, None]:
    """
    Asynchronous generator that yields a random number
    between 0 and 10 after waiting for 1 second in
    each iteration. It loops 10 times.

    Yields:
        int: A random integer between 0 and 10.

    Usage:
    ```python
    async def example_usage():
        async for number in async_generator():
            print(number)
    ```
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
