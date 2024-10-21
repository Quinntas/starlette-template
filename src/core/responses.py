from starlette.responses import JSONResponse

from src.core.context import Context
from src.core.json import json


def json_response(ctx: Context, status_code: int, body: json) -> None:
    del ctx.response.headers['content-length']
    ctx.response = JSONResponse(body, status_code, headers=ctx.response.headers)


internal_server_error = JSONResponse({'message': 'Internal Server Error'}, status_code=500)

not_found = JSONResponse({'message': 'Not Found'}, status_code=404)

bad_request = JSONResponse({'message': 'Bad Request'}, status_code=400)

unauthorized = JSONResponse({'message': 'Unauthorized'}, status_code=401)

forbidden = JSONResponse({'message': 'Forbidden'}, status_code=403)
