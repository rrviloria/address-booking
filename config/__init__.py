import os

from dotenv import load_dotenv

BASEDIR = "/".join(os.path.abspath(os.path.dirname(__file__)).split("/")[:-1])
load_dotenv(os.path.join(BASEDIR, ".env"))

settings_file = os.getenv("SETTINGS_FILE", "local")

if settings_file == "local":
    from .local import *
if settings_file == "staging":
    from .staging import *
if settings_file == "prod":
    from .prod import *
