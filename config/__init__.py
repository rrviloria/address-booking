import os

settings_file = os.getenv("SETTINGS_FILE", "local")

if settings_file == "local":
    from .local import *
if settings_file == "staging":
    from .staging import *
if settings_file == "prod":
    from .prod import *
