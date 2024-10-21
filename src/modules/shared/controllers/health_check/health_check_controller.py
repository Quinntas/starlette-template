from src.core.context import Context
from src.core.responses import json_response


async def health_check_controller(ctx: Context):
    json_response(ctx, 200, {'message': 'ok'})
