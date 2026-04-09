from fastapi import FastAPI
from contextlib import asynccontextmanager
from fastapi.exceptions import ResponseValidationError
from pydantic_core._pydantic_core import ValidationError
from sqlalchemy.exc import IntegrityError
from .booking import routes as booking_routes
from .oauth import routes as oauth_routes
from .core.database import create_db_and_tables
from .core.exception_handler import custom_validation_error, custom_integrity_error


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield


app = FastAPI(lifespan=lifespan)


app.include_router(booking_routes.router)
app.include_router(oauth_routes.router)

app.add_exception_handler(ValidationError, custom_validation_error)
app.add_exception_handler(ResponseValidationError, custom_validation_error)
app.add_exception_handler(IntegrityError, custom_integrity_error)
# add more custom exception handler in the future
