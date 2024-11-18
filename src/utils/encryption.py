from passlib.hash import pbkdf2_sha256

from src.utils.env import PEPPER


def encrypt_with_pbkdf2_sha256(content: str) -> str:
    return pbkdf2_sha256.hash(PEPPER + content)


def verify_with_pbkdf2_sha256(left: str, right: str) -> bool:
    return pbkdf2_sha256.verify(PEPPER + left, right)
