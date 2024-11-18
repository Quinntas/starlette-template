import pickle
from typing import Type, TypeVar, Optional, Any, List, Union

from src.core.cache import Cache
from src.modules.shared.infra.base_model import BaseModel

T = TypeVar("T", bound=BaseModel)


class CacheConfig:
    def __init__(self, key: str, expires_in: int = 3600):
        self.key = key
        self.expires_in = expires_in


class Repository:
    def __init__(self, cache: Cache):
        self.cache = cache

    @staticmethod
    async def insert(model_instance: BaseModel) -> None:
        await model_instance.save()

    async def _get_from_cache(self, model_class: Type[T], key: str) -> Union[Optional[T], List[T]]:
        cached_data = await self.cache.get(key)
        if cached_data:
            data = pickle.loads(cached_data)
            if isinstance(data, list):
                return [model_class.deserialize(item) for item in data]
            return model_class.deserialize(data)
        return None

    async def _set_to_cache(self, key: str, data: Any, expires_in: int) -> None:
        if isinstance(data, list):
            serialized_data = pickle.dumps([item.serialize() for item in data])
        else:
            serialized_data = pickle.dumps(data.serialize())
        await self.cache.set(key, serialized_data, expires_in)

    async def filter_with_params(self, model_class: Type[T], cache_config: Optional[CacheConfig] = None, **kwargs):
        return await self.select(
            model_class,
            model_class.filter(**kwargs),
            cache_config
        )

    async def update(self, model_class: Type[T], id: int, **kwargs) -> None:
        await model_class.filter(id=id).update(**kwargs)

    async def delete(self, model_class: Type[T], id: int) -> None:
        await model_class.filter(id=id).delete()

    async def upsert(self, model_instance: BaseModel) -> None:
        await model_instance.save(update_fields=model_instance.meta.fields_map.keys())

    async def select(
            self,
            model_class: Type[T],
            query: Any,
            cache_config: Optional[CacheConfig] = None,
    ) -> list[T]:
        if cache_config:
            cached_result = await self._get_from_cache(model_class, cache_config.key)
            if cached_result is not None:
                return cached_result

        result = await query

        if result is None:
            raise Exception("No records found")

        if result and cache_config:
            await self._set_to_cache(cache_config.key, result, cache_config.expires_in)

        return result
