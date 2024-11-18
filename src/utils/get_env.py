# type: ignore

from typing import TypeVar

from decouple import config

T = TypeVar("T")


def get_env(key: str, default=None, required=True, cast=str) -> T:
    value = config(key) or default
    if required and value is None:
        raise ValueError(f"Missing required environment variable: {key}")
    return cast(value)
