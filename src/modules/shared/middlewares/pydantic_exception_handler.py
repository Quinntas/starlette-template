from abc import ABC

from pydantic import ValidationError

from src.core.context import Context
from src.core.middleware import Middleware
from src.core.responses import json_response
from src.core.typings import next_func


class PydanticExceptionHandlerMiddleware(Middleware, ABC):
    async def handle(self, ctx: Context, call_next: next_func):
        try:
            await call_next()
        except ValidationError as e:
            return json_response(
                ctx, 422, {"message": "Validation error", "errors": e.errors()}
            )
