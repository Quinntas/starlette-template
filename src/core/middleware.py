from typing import Callable, Awaitable

from src.core.context import Context

middleware_func = Callable[[Context, Callable[[], Awaitable[None]]], Awaitable[None]]
