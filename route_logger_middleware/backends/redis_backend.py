import logging

from . import QueueBackend

try:
    import aioredis
except ImportError:
    logging.warning("Redis not found. Install using pip install aioredis")
    aioredis = None


class RedisBackend(QueueBackend):
    def __init__(self, redis_uri: str, db: int):
        self.redis_conn = aioredis.from_url(redis_uri, db=db)

    async def send_message(self, message):
        self.redis_conn.hset(message)
