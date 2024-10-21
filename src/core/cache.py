from typing import Any

import redis


class Cache:
    def __init__(self, host: str, port: int):
        self.cache = redis.Redis(host=host, port=port, decode_responses=True)

    def set(self, key: str, value: Any, expires_in: int = 3600):
        self.cache.set(key, value, ex=expires_in)

    def get(self, key: str) -> Any:
        return self.cache.get(key)
