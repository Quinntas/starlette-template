from src.modules.shared.infra.base_model import BaseModel


class BaseDTO(BaseModel):
    class Config:
        validate_assignment = True
