import aiopg

dsn = "dbname=postgres user=root password=rootpwd host=localhost port=5432"


async def get_db_connection():
    return await aiopg.connect(dsn)
