import os
from dotenv import load_dotenv

BASEDIR = "/".join(os.path.abspath(os.path.dirname(__file__)).split("/")[:-1])
load_dotenv(os.path.join(BASEDIR, '.env'))

APP_SECRET_KEY = os.getenv("APP_SECRET_KEY")

SQLITE_DB_NAME = os.getenv("SQLITE_DB_NAME")
SQLITE_URL = f"sqlite:///{SQLITE_DB_NAME}"

JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
JWT_ALGORITHM = os.getenv("JWT_ALGORITHM")
JWT_ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("JWT_ACCESS_TOKEN_EXPIRE_MINUTES", 30))
