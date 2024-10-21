import time

from src.core.context import Context
from src.core.next import next_func


async def performance_middleware(ctx: Context, call_next: next_func) -> None:
    start_time = time.time()
    await call_next()
    end_time = time.time()
    ctx.response.headers.update({
        'X-Response-Time': str(end_time - start_time)
    })
