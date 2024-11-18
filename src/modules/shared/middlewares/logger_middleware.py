from abc import ABC
from datetime import datetime

from src.core.context import Context
from src.core.middleware import Middleware
from src.core.typings import next_func


class LoggerMiddleware(Middleware, ABC):
    async def handle(self, ctx: Context, call_next: next_func):
        req_ip = ctx.request.client.host
        date = datetime.now().strftime("%d/%b/%Y %H:%M:%S")
        log_entry = f'{req_ip} - - [{date}] "{ctx.request.method} {ctx.request.url} {ctx.request.headers.get("user-agent")}"'
        print(log_entry)
        await call_next()
