from abc import ABC, abstractmethod
from typing import Awaitable

from src.core.context import Context
from src.core.typings import next_func


class Middleware(ABC):
    @abstractmethod
    async def handle(self, ctx: Context, call_next: next_func) -> Awaitable[None]:
        pass
