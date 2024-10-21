from typing import List

from starlette.routing import Route

from src.core.base_controller import base_controller
from src.core.controller import controller_func
from src.core.middleware import middleware_func


class Router:
    def __init__(self):
        self.routes: List[Route] = []
        self.middlewares: List[middleware_func] = []

    def add_middleware(self, middleware: middleware_func):
        self.middlewares.append(middleware)

    def add_route(self, path: str, controller: controller_func, methods: List[str], middlewares: List | None = None):
        self.routes.append(
            Route(path,
                  base_controller(controller, self.middlewares + (middlewares if middlewares is not None else [])),
                  methods=methods)
        )

    def get(self, path: str, controller, middlewares: List | None = None):
        self.add_route(path, controller, ['GET'], middlewares)

    def post(self, path: str, controller, middlewares: List | None = None):
        self.add_route(path, controller, ['POST'], middlewares)

    def put(self, path: str, controller, middlewares: List | None = None):
        self.add_route(path, controller, ['PUT'], middlewares)

    def delete(self, path: str, controller, middlewares: List | None = None):
        self.add_route(path, controller, ['DELETE'], middlewares)
