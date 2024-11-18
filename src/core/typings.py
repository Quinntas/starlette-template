from typing import Callable, Awaitable
from typing import Mapping

next_func = Callable[[], Awaitable[None]]

json = Mapping[str, str | int | float | bool | None]
