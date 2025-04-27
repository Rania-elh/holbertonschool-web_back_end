#!/usr/bin/env python3
"""Tasks example."""
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Create a task that waits for a random delay.

    Args:
        max_delay (int): Maximum delay in seconds

    Returns:
        asyncio.Task: A task that waits for a random delay
    """
    task = asyncio.create_task(wait_random(max_delay))
    return task
