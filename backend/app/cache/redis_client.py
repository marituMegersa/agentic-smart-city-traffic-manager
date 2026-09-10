import redis
import os

redis_url = os.getenv("REDIS_URL", "redis://localhost:6379/0")
redis_client = redis.Redis.from_url(redis_url)

def get_cached_agent_response(key: str):
    return redis_client.get(key)

def cache_agent_response(key: str, value: str, ttl: int = 3600):
    redis_client.setex(key, ttl, value)
