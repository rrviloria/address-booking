import logging
from typing import Callable
from fastapi import Request, Response
from fastapi.routing import APIRoute


logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class RouteLogger(APIRoute):
    """Custom Route which logs POST/PATCH request data and response
    for debugging purposes
    """

    def get_route_handler(self, *args, **kwargs) -> Callable:
        original_route_handler = super().get_route_handler(*args, **kwargs)

        async def custom_route_handler(request: Request, *args, **kwargs) -> Response:
            method = request.method
            if method in ["POST", "PATCH"]:
                body = await request.body()
                logger.info(f"Request body: {body.decode()}")

            response: Response = await original_route_handler(request)

            if method in ["POST", "PATCH"]:
                logger.info(f"Response body: {response.body.decode()}")
            return response

        return custom_route_handler
