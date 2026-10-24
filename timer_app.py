from typing import Callable
import time
from functools import wraps


def timer(rep: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            start = time.perf_counter()
            for _ in range(rep):
                result = func(*args, **kwargs)
            end = time.perf_counter()
            print(f"{func.__name__} took {end - start:.6f} seconds")
            return result
        return wrapper
    return decorator
