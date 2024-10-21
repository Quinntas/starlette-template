from datetime import datetime

from src.modules.shared.infra.base_model import BaseModel


class UserModel(BaseModel):
    id: int
    pid: str
    created_at: datetime
    email: str
    password: str
