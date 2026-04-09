from fastapi import Request, status
from pydantic_core._pydantic_core import ValidationError
from sqlalchemy.exc import IntegrityError
from fastapi.responses import JSONResponse
from .loggger import logger


async def custom_validation_error(request: Request, exc: ValidationError):
    """Custom handling for validation error where we also logs the error
    """
    err = {"detail": "Error encountered", "errors": exc.errors()}
    logger.debug(err)
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=err,
    )

async def custom_integrity_error(request: Request, exc: IntegrityError):
    """Custom handling for validation error where we also logs the error
    """
    err = {"detail": "Error encountered", "errors": ["Integrity error unique field"]}
    logger.debug(err)
    return JSONResponse(
        status_code=500,
        content=err,
    )

# TODO: Add more validation handling
