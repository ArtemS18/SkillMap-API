from hashlib import md5
from typing import Any, Callable, Coroutine, TypeVar
from redis_client.client import get_client
from functools import wraps
import pickle

T = TypeVar("AsyncFunc", bound=Callable[..., Coroutine[Any, Any, Any]])
CHACHING_TIME = 600


def cache_query(time_limit: int = CHACHING_TIME, caching=True):
    def decorator(func: T) -> T:
        @wraps(func)
        async def wrapper(*args, **kwargs):
            redis = get_client()
            if caching:
                args_hash = md5(
                    str(
                        args + tuple(sorted(kwargs.items(), key=lambda x: x[0]))
                    ).encode()
                ).hexdigest()

                key = f"cache:{func.__name__}:{args_hash}"
                raw = await redis.get(key)
                if raw is not None:
                    print(f"HIT: {key}")
                    return pickle.loads(raw)
                else:
                    print(f"MISS: {key}")
            res = await func(*args, **kwargs)
            if caching:
                await redis.setex(key, time_limit, pickle.dumps(res))
            return res

        return wrapper

    return decorator
