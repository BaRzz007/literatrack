from sqlalchemy import URL
from os import getenv

password = getenv("PASSWORD")
db_user = getenv("DB_USER")
host = getenv("HOST", default='localhost')
database = getenv("DB_NAME")

url_object = URL.create(
        "mysql+mysqldb",
        username=db_user,
        password=password,
        host=host,
        database=database)
