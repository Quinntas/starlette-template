from abc import ABC, abstractmethod
from typing import Awaitable

from src.core.context import Context


class Controller(ABC):
    @abstractmethod
    async def handle(self, ctx: Context) -> Awaitable[None]:
        pass
