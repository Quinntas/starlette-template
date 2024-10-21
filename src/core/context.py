from typing import Any

from starlette.requests import Request
from starlette.responses import Response


class Context:
    def __init__(self, request: Request, response: Response, state: dict[str, Any]):
        self.request = request
        self.response = response
        self.state = state
