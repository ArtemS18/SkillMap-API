from hashlib import md5
from logging import getLogger
from typing import Any, Callable, Coroutine, TypeVar
from redis_client.client import get_client
from functools import wraps
import pickle

T = TypeVar("AsyncFunc", bound=Callable[..., Coroutine[Any, Any, Any]])
CHACHING_TIME = 600

log = getLogger(__name__)


def cache_query(time_limit: int = CHACHING_TIME, caching=True):
    def decorator(func: T) -> T:
        @wraps(func)
        async def wrapper(*args, **kwargs):
            redis = get_client()
            if not caching:
                return await func(*args, **kwargs)
            args_hash = md5(
                str(args + tuple(sorted(kwargs.items(), key=lambda x: x[0]))).encode()
            ).hexdigest()

            key = f"cache:{func.__name__}:{args_hash}"
            raw = await redis.get(key)
            if raw is None:
                log.info(f"FIRST MISS: {key}")
                lock = redis.lock(f"lock:{key}", timeout=5)
                acqured = await lock.acquire(blocking_timeout=3)
                try:
                    raw = await redis.get(key)
                    if raw is not None:
                        return pickle.loads(raw)
                    log.info(f"SECOND MISS: {key}")
                    res = await func(*args, **kwargs)
                    await redis.setex(key, time_limit, pickle.dumps(res))
                    return res
                finally:
                    if acqured:
                        await lock.release()
            else:
                log.info(f"HIT: {key}")
                return pickle.loads(raw)

        return wrapper

    return decorator
