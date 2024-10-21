import aiopg

from src.core.repository import Repository
from src.modules.user.infra.user_model import UserModel

CREATE_USER = """
INSERT INTO Users (pid, email, password)
VALUES (%s, %s, %s)
"""

GET_WITH_EMAIL = """
SELECT * FROM Users WHERE email = %s
"""


class UserRepository(Repository):
    def __init__(self, database: aiopg.Connection):
        super().__init__(database)

    async def create_user(self, pid: str, email: str, password: str):
        await self.insert(CREATE_USER, (pid, email, password))

    async def get_with_email(self, email: str):
        return await self.select_one(UserModel, GET_WITH_EMAIL, (email))
