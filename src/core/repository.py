from typing import Type, TypeVar, Optional

import aiopg

from src.modules.shared.infra.base_model import BaseModel

T = TypeVar('T', bound=BaseModel)


class Repository:
    def __init__(self, database: aiopg.Connection):
        self.database = database

    async def insert(self, query: str, params: tuple):
        async with self.database.cursor() as cursor:
            await cursor.execute(query, params)
            await self.database.commit()

    async def select_one(self, model: Type[T], query: str, params: tuple) -> Optional[T]:
        async with self.database.cursor() as cursor:
            await cursor.execute(query, params)
            result = await cursor.fetchone()
            if result:
                return model(**dict(result))
            return None

    async def select_all(self, model: Type[T], query: str, params: tuple) -> list[T]:
        async with self.database.cursor() as cursor:
            await cursor.execute(query, params)
            result = await cursor.fetchall()
            return [model(**dict(row)) for row in result]
