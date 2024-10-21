from typing import List
from urllib.request import Request

from starlette.responses import Response

from src.core.context import Context
from src.core.controller import controller_func
from src.core.middleware import middleware_func
from src.core.responses import internal_server_error


def base_controller(
        handler: controller_func,
        middlewares: List[middleware_func] | None = None):
    async def base_handler(request: Request) -> Response | None:
        ctx = Context(request, internal_server_error, {})

        if middlewares is None or len(middlewares) == 0:
            await handler(ctx)
        else:
            async def call_next(index: int):
                if index < len(middlewares):
                    return await middlewares[index](ctx, lambda: call_next(index + 1))
                else:
                    await handler(ctx)

            await call_next(0)

        return ctx.response

    return base_handler
