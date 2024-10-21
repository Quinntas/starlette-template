from typing import Callable, Awaitable

next_func = Callable[[], Awaitable[None]]
