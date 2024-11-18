from abc import ABC

from src.core.context import Context
from src.core.controller import Controller
from src.core.responses import json_response


class HealthCheckController(Controller, ABC):
    async def handle(self, ctx: Context):
        return json_response(ctx, 200, {"status": "ok"})
