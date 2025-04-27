#!/usr/bin/env python3
"""Basic async syntax example."""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Wait for a random delay between 0 and max_delay seconds.

    Args:
        max_delay (int): Maximum delay in seconds (default: 10)

    Returns:
        float: The actual delay that was waited
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
