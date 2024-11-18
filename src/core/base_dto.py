from pydantic import BaseModel


class BaseDTO(BaseModel):
    class Config:
        validate_assignment = True
        arbitrary_types_allowed = True
