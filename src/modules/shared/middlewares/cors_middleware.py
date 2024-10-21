from src.core.context import Context
from src.core.next import next_func


async def cors_middleware(ctx: Context, call_next: next_func) -> None:
    ctx.response.headers.update({
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'GET, POST, PUT, DELETE, OPTIONS',
        'Access-Control-Allow-Headers': 'Content-Type'
    })
    await call_next()
