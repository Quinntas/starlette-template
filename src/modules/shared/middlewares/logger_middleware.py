from datetime import datetime

from src.core.context import Context
from src.core.next import next_func


async def logger_middleware(ctx: Context, call_next: next_func) -> None:
    req_ip = ctx.request.client.host
    date = datetime.now().strftime('%d/%b/%Y %H:%M:%S')
    log_entry = f'{req_ip} - - [{date}] "{ctx.request.method} {ctx.request.url} {ctx.request.headers.get("user-agent")}"'
    print(log_entry)
    await call_next()
