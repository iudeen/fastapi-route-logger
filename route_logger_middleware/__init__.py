"""



author: irfanuddin
github: @iudeen
"""
import json
import logging
import typing
import asyncio

from starlette.middleware.base import DispatchFunction
from starlette.types import ASGIApp

from route_logger_middleware.backends import QueueBackend

logger = logging.getLogger("logging-middleware")

try:
    from fastapi import Response
    from starlette.middleware.base import BaseHTTPMiddleware
    from starlette.requests import Request
except ImportError:
    logging.warning("FastAPI not installed, import error. Run pip install fastapi")
    Response = BaseHTTPMiddleware = Request = None


class GlobalLoggerMiddleware(BaseHTTPMiddleware):
    def __init__(
            self, app: ASGIApp,
            dispatch: typing.Optional[DispatchFunction] = None,
            *,
            backend: QueueBackend,
            module_name: str
    ):
        super().__init__(app=app, dispatch=dispatch)
        self.backend = backend
        self.module_name = module_name

    async def dispatch(self, request: Request, call_next: typing.Callable) -> Response:
        receive_ = await request.receive()

        log_dict = {
            "module": self.module_name,
            "url": request.url.netloc,
            "path": request.url.path,
            "method": request.method,
            "cookies": dict(request.cookies),
            "path_params": request.path_params,
            "query_params": request.query_params.__dict__,
            "body": receive_.get('body').decode(),
            "client": request.client.host
        }
        loop = asyncio.get_event_loop()
        loop.create_task(self.backend.send_message(json.dumps(log_dict)))
        return await call_next(request)
