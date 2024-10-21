from datetime import datetime
from typing import Callable, Any

from starlette.applications import Starlette
from starlette.requests import Request
from starlette.responses import JSONResponse, Response
from starlette.routing import Route
from starlette.types import ASGIApp


class Context:
    def __init__(self, request: Request, response: Response | None, state: dict[str, Any]):
        self.request = request
        self.response = response
        self.state = state


async def logging_middleware(ctx: Context, call_next: Callable) -> Any:
    req_ip = ctx.request.client.host
    date = datetime.now().strftime('%d/%b/%Y %H:%M:%S')
    log_entry = f'{req_ip} - - [{date}] "{ctx.request.method} {ctx.request.url} {ctx.request.headers.get("user-agent")}"'
    print(log_entry)
    await call_next()


async def hello_world_controller(ctx: Context):
    ctx.response = JSONResponse({'hello': 'world', 'state': ctx.state})


def base_controller(
        handler: Callable[[Context], Any],
        middlewares=None):
    async def base_handler(request: Request) -> Response | None:
        ctx = Context(request, None, {})

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


app: ASGIApp = Starlette(
    debug=False,
    routes=[
        Route('/',
              base_controller(hello_world_controller, [logging_middleware]),
              methods=['GET']),
    ],
)
