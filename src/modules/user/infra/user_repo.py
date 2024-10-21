import aiopg

from src.core.repository import Repository

CREATE_USER = """
INSERT INTO Users (pid, email, password)
VALUES (%s, %s, %s)
"""


class UserRepository(Repository):
    def __init__(self, database: aiopg.Connection):
        super().__init__(database)

    async def create_user(self, pid: str, email: str, password: str):
        await self.insert(CREATE_USER, (pid, email, password))
