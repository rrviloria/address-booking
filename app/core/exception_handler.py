from fastapi import Request, status
from pydantic_core._pydantic_core import ValidationError
from fastapi.responses import JSONResponse
from .loggger import logger


async def custom_validation_error(request: Request, exc: ValidationError):
    err = {"detail": "Error encountered", "errors": exc.errors()}
    logger.debug(err)
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=err,
    )
