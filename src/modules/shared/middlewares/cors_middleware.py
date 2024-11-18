from abc import ABC

from src.core.context import Context
from src.core.middleware import Middleware
from src.core.typings import next_func


class CorsMiddleware(Middleware, ABC):
    async def handle(self, ctx: Context, call_next: next_func):
        ctx.response.headers.update({
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "*",
            "Access-Control-Allow-Headers": "*",
        })
        return await call_next()
