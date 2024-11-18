from typing import Any

import aioredis


class Cache:
    def __init__(self, host: str, port: int):
        self.client = aioredis.from_url(
            f"redis://{host}:{port}", decode_responses=False
        )

    async def set(
            self, key: str, value: str | int | float | bytes, expires_in: int = 3600
    ):
        await self.client.set(key, value, ex=expires_in)

    async def get(self, key: str) -> Any:
        return await self.client.get(key)
