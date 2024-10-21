from starlette.applications import Starlette
from starlette.types import ASGIApp

from src.infra.routes import router

app: ASGIApp = Starlette(
    debug=False,
    routes=router.routes,
)
