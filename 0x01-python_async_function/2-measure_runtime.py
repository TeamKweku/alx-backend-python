#!/usr/bin/env python3
"""module that imports wait_N and implements a function
that measure the runtime"""

import asyncio
import time
from typing import List

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time for wait_n and
    returns the average time per call.

    Parameters:
    - n (int): The number of times to spawn wait_random.
    - max_delay (int): The maximum delay for wait_random.

    Returns:
    - float: The average time per call.
    """

    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()
    total_time = end_time - start_time
    return total_time / n
