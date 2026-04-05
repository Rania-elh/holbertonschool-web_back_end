#!/usr/bin/env python3
"""Redis cache: store arbitrary string-like or numeric values."""
import uuid
from functools import wraps
import redis
from typing import Any, Callable, Optional, Union


def count_calls(method: Callable[..., Any]) -> Callable[..., Any]:
    """Increment a Redis counter keyed by the method's qualified name on each call."""
    qn = method.__qualname__

    @wraps(method)
    def wrapper(self: Any, *args: Any, **kwargs: Any) -> Any:
        self._redis.incr(qn)
        return method(self, *args, **kwargs)

    return wrapper


def call_history(method: Callable[..., Any]) -> Callable[..., Any]:
    """Append each call's args and return value to Redis lists keyed by qualname."""
    qn = method.__qualname__

    @wraps(method)
    def wrapper(self: Any, *args: Any, **kwargs: Any) -> Any:
        self._redis.rpush(f"{qn}:inputs", str(args))
        output = method(self, *args, **kwargs)
        self._redis.rpush(f"{qn}:outputs", output)
        return output

    return wrapper


class Cache:
    """Simple Redis-backed key-value cache."""

    def __init__(self) -> None:
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(
        self,
        key: str,
        fn: Optional[Callable[[bytes], Any]] = None,
    ) -> Optional[Any]:
        data = self._redis.get(key)
        if data is None:
            return None
        if fn is not None:
            return fn(data)
        return data

    def get_str(self, key: str) -> Optional[str]:
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> Optional[int]:
        return self.get(key, fn=int)


def replay(method: Callable[..., Any]) -> None:
    """Print stored input/output history for a bound Cache method."""
    r = method.__self__._redis
    qn = method.__qualname__
    inputs = r.lrange(f"{qn}:inputs", 0, -1)
    outputs = r.lrange(f"{qn}:outputs", 0, -1)
    print(f"{qn} was called {len(inputs)} times:")
    for inp, out in zip(inputs, outputs):
        print(f"{qn}(*{inp.decode('utf-8')}) -> {out.decode('utf-8')}")
