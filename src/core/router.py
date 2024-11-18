from typing import List

from starlette.routing import Route

from src.core.controller import Controller
from src.core.http_handler import http_handler
from src.core.middleware import Middleware


class Router:
    def __init__(self):
        self.routes: List[Route] = []
        self.middlewares: List[Middleware] = []

    def add_middleware(self, middleware: Middleware):
        self.middlewares.append(middleware)

    def add_route(
            self,
            path: str,
            controller: Controller,
            methods: List[str],
            middlewares: List | None = None,
    ):
        self.routes.append(
            Route(
                path,
                http_handler(
                    controller,
                    self.middlewares + (middlewares if middlewares is not None else []),
                ),
                methods=methods,
            )
        )

    def get(self, path: str, controller, middlewares: List | None = None):
        self.add_route(path, controller, ["GET"], middlewares)

    def post(self, path: str, controller, middlewares: List | None = None):
        self.add_route(path, controller, ["POST"], middlewares)

    def put(self, path: str, controller, middlewares: List | None = None):
        self.add_route(path, controller, ["PUT"], middlewares)

    def delete(self, path: str, controller, middlewares: List | None = None):
        self.add_route(path, controller, ["DELETE"], middlewares)
