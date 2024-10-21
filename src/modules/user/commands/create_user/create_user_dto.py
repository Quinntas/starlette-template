from src.modules.shared.controllers.base_dto import BaseDTO


class CreateUserDTO(BaseDTO):
    email: str
    password: str
