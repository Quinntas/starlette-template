from typing import Callable, Awaitable

from src.core.context import Context

controller_func = Callable[[Context], Awaitable[None]]
