from fastapi import FastAPI
from fastapi.exceptions import ResponseValidationError
from pydantic_core._pydantic_core import ValidationError
from .booking import routes as booking_routes
from .oauth import routes as oauth_routes
from .core.database import *
from .core.exception_handler import (
    custom_validation_error,
)


app = FastAPI()


@app.on_event("startup")
def on_startup():
    create_db_and_tables()


app.include_router(booking_routes.router)
app.include_router(oauth_routes.router)

app.add_exception_handler(ValidationError, custom_validation_error)
app.add_exception_handler(ResponseValidationError, custom_validation_error)
# add more custom exception handler in the future
