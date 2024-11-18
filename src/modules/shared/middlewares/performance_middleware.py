import time
from abc import ABC

from src.core.context import Context
from src.core.middleware import Middleware
from src.core.typings import next_func


class PerformanceMiddleware(Middleware, ABC):
    async def handle(self, ctx: Context, call_next: next_func):
        start_time = time.time()
        await call_next()
        end_time = time.time()
        ctx.response.headers.update({"X-Response-Time": str(end_time - start_time)})
