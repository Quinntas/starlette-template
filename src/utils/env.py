from src.utils.get_env import get_env

DB_NAME: object = get_env("DB_NAME")
DB_USER: str = get_env("DB_USER")
DB_PASSWORD: str = get_env("DB_PASSWORD")
DB_HOST: str = get_env("DB_HOST")
DB_PORT: str = get_env("DB_PORT")

REDIS_HOST: str = get_env("REDIS_HOST")
REDIS_PORT: int = get_env("REDIS_PORT", cast=int)

JWT_SECRET: str = get_env("JWT_SECRET")
PEPPER: str = get_env("PEPPER")

PORT: int = get_env("PORT", 3000, cast=int)
