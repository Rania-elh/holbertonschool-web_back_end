#!/usr/bin/env python3
"""Module that defines an async generator producing 10 random float numbers."""

import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    Yield 10 random float numbers between 0 and 10,
    one every second using asyncio.sleep.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)

