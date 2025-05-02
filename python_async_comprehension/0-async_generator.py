#!/usr/bin/env python3

import asyncio
import random
from typing import AsyncGenerator

async def async_generator() -> AsyncGenerator[float, None]:
    """
    Async generator that yields 10 random float numbers between 0 and 10.
    Each random number is yielded after waiting for 1 second.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)  # Génère un nombre flottant aléatoire entre 0 et 10
