# 0x01. Python - Async

> This repo contains source code on the use of Python asyncio module

## Contents

1. [Basic Asynchronous Syntax](0-basic_async_syntax.py)

   - An asynchronous coroutine that waits for a random delay between 0 and max_delay seconds.

   ```python
   #!/usr/bin/env python3

   import asyncio

   wait_random = __import__('0-basic_async_syntax').wait_random

   print(asyncio.run(wait_random()))
   print(asyncio.run(wait_random(5)))
   print(asyncio.run(wait_random(15)))
   ```

2. [Concurrent Coroutines](1-concurrent_coroutines.py)

   - An async routine that spawns wait_random n times with the specified max_delay.
   - Returns a list of all the delays (float values) in ascending order.

   ```python
   #!/usr/bin/env python3

   import asyncio

   wait_n = __import__('1-concurrent_coroutines').wait_n

   print(asyncio.run(wait_n(5, 5)))
   print(asyncio.run(wait_n(10, 7)))
   print(asyncio.run(wait_n(10, 0)))
   ```

3. [Measure Runtime](2-measure_runtime.py)

   - Measures the total execution time for wait_n(n, max_delay) and returns total_time / n.

   ```python
   #!/usr/bin/env python3

   measure_time = __import__('2-measure_runtime').measure_time

   n = 5
   max_delay = 9

   print(measure_time(n, max_delay))
   ```

4. [Asyncio Tasks](3-tasks.py)

   - Function `task_wait_random` that returns an asyncio.Task for wait_random.

   ```python
   #!/usr/bin/env python3

   import asyncio

   task_wait_random = __import__('3-tasks').task_wait_random

   async def test(max_delay: int) -> float:
       task = task_wait_random(max_delay)
       await task
       print(task.__class__)

   asyncio.run(test(5))
   ```

5. [Asyncio Task Wait N](4-tasks.py)

   - Function `task_wait_n` that uses `task_wait_random` to spawn tasks for wait_random.

   ```python
   #!/usr/bin/env python3

   import asyncio

   task_wait_n = __import__('4-tasks').task_wait_n

   n = 5
   max_delay = 6
   print(asyncio.run(task_wait_n(n, max_delay)))
   ```

Feel free to explore and run these scripts to better understand asynchronous programming in Python.

---

**Note:** The file paths in the commands are relative to the root of your repository.
