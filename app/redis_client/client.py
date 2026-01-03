from redis.asyncio import Redis
from config import settings

_client = Redis.from_url(url=settings.redis_connection_string)


def get_client():
    return _client


async def disconnect():
    await _client.close()
