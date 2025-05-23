#!/usr/bin/env python3

"""
Coroutine that collects 10 random float numbers from an async generator.
Uses an async comprehension over async_generator.
"""

from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Collects 10 random float numbers using an async comprehension
    over async_generator and returns them in a list.
    """
    return [i async for i in async_generator()]
