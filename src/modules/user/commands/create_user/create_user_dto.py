class CreateUserDTO:
    def __init__(self, username: str, password: str, email: str):
        self.username = username
        self.password = password
        self.email = email


class CreateUserResponseDTO:
    def __init__(self, user_id: int):
        self.user_id = user_id
