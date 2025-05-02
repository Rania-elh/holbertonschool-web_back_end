#!/usr/bin/env python3

"""
Coroutine that measures the time taken to execute async_comprehension 4 times in parallel.
"""

import asyncio
import time
from async_comprehension import async_comprehension  # Assure-toi que le nom est correct


async def measure_runtime() -> float:
    """
    Runs async_comprehension 4 times in parallel using asyncio.gather(),
    measures the total time taken, and returns it.
    """
    start_time = time.time()  # Temps avant le démarrage
    # Lancer les 4 coroutines en parallèle
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )
    return time.time() - start_time  # Temps après les 4 exécutions, retourne la différence
