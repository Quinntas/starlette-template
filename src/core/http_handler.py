from typing import List
from urllib.request import Request

from starlette.responses import Response

from src.core.context import Context
from src.core.controller import Controller
from src.core.middleware import Middleware
from src.core.responses import internal_server_error


def http_handler(controller: Controller, middlewares: List[Middleware] | None = None):
    async def base_handler(request: Request) -> Response | None:
        ctx = Context(request, internal_server_error, {})

        if middlewares is None or len(middlewares) == 0:
            await controller.handle(ctx)
        else:

            async def call_next(index: int):
                if index < len(middlewares):
                    return await middlewares[index].handle(
                        ctx, lambda: call_next(index + 1)
                    )
                else:
                    await controller.handle(ctx)

            await call_next(0)

        return ctx.response

    return base_handler
