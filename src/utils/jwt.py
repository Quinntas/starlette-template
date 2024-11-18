from datetime import datetime, timedelta
from typing import Any, Dict

import jwt
from src.utils.env import JWT_SECRET

ALGORITHM = "HS256"


def sign_jwt(data: Dict[str, Any], expires_in: int = 60 * 60) -> str:
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(seconds=expires_in)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, JWT_SECRET, algorithm=ALGORITHM)
    return encoded_jwt


def decode_jwt(token: str) -> Dict[str, Any] | None:
    try:
        decoded_token = jwt.decode(token, JWT_SECRET, algorithms=[ALGORITHM])
        return (
            decoded_token
            if decoded_token["exp"] >= datetime.utcnow().timestamp()
            else None
        )
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None
