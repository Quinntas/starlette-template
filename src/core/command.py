from abc import ABC, abstractmethod
from typing import Awaitable

from src.core.base_dto import BaseDTO


class Command(ABC):
    @abstractmethod
    async def handle(self, dto: BaseDTO) -> Awaitable[None]:
        pass
