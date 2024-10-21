from src.core.router import Router
from src.modules.shared.controllers.health_check.health_check_controller import health_check_controller
from src.modules.shared.middlewares.cors_middleware import cors_middleware
from src.modules.shared.middlewares.logger_middleware import logger_middleware
from src.modules.shared.middlewares.performance_middleware import performance_middleware
from src.modules.user.commands.create_user.create_user_controller import create_user_controller

router = Router()

router.add_middleware(performance_middleware)
router.add_middleware(logger_middleware)
router.add_middleware(cors_middleware)

router.get('/', health_check_controller)

router.post('/users', create_user_controller)
