from src.core.router import Router

router = Router()

router.add_middleware(performance_middleware)
router.add_middleware(logger_middleware)
router.add_middleware(cors_middleware)

router.get('/', health_check_controller)
