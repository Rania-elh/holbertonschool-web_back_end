#!/usr/bin/env python3
"""
Take the code from wait_n and alter it into a new function task_wait_n.
The code is nearly identical to wait_n except task_wait_random is being called.
"""
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Let's execute multiple tasks at the same time with async
    """
    delays = []
    tasks = []

    for _ in range(n):
        task = await task_wait_random(max_delay)  # on attend pour récupérer la vraie Task
        tasks.append(task)

    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)

    return delays

