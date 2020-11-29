"""
This type stub file was generated by pyright.
"""

from typing import Any, Callable, Dict, List, Optional, Sequence, Type, Union
from fastapi import routing
from fastapi.encoders import DictIntStrAny, SetIntStr
from fastapi.params import Depends
from starlette.applications import Starlette
from starlette.middleware import Middleware
from starlette.responses import Response
from starlette.routing import BaseRoute
from starlette.types import Receive, Scope, Send


class FastAPI(Starlette):
    def __init__(self, *, debug: bool = ..., routes: Optional[List[BaseRoute]] = ..., title: str = ..., description: str = ..., version: str = ..., openapi_url: Optional[str] = ..., openapi_tags: Optional[List[Dict[str, Any]]] = ..., servers: Optional[List[Dict[str, Union[str, Any]]]] = ..., default_response_class: Type[Response] = ..., docs_url: Optional[str] = ..., redoc_url: Optional[str] = ..., swagger_ui_oauth2_redirect_url: Optional[str] = ..., swagger_ui_init_oauth: Optional[dict] = ..., middleware: Optional[Sequence[Middleware]] = ..., exception_handlers: Optional[Dict[Union[int, Type[Exception]], Callable]] = ..., on_startup: Optional[Sequence[Callable]] = ..., on_shutdown: Optional[Sequence[Callable]] = ..., openapi_prefix: str = ..., root_path: str = ..., root_path_in_servers: bool = ..., **extra: Any) -> None:
        ...

    def openapi(self) -> Dict:
        ...

    def setup(self) -> None:
        ...

    async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None:
        ...

    def add_api_route(self, path: str, endpoint: Callable, *, response_model: Optional[Type[Any]] = ..., status_code: int = ..., tags: Optional[List[str]] = ..., dependencies: Optional[Sequence[Depends]] = ..., summary: Optional[str] = ..., description: Optional[str] = ..., response_description: str = ..., responses: Optional[Dict[Union[int, str], Dict[str, Any]]] = ..., deprecated: Optional[bool] = ..., methods: Optional[List[str]] = ..., operation_id: Optional[str] = ..., response_model_include: Optional[Union[SetIntStr, DictIntStrAny]] = ..., response_model_exclude: Optional[Union[SetIntStr, DictIntStrAny]] = ..., response_model_by_alias: bool = ..., response_model_exclude_unset: bool = ..., response_model_exclude_defaults: bool = ..., response_model_exclude_none: bool = ..., include_in_schema: bool = ..., response_class: Optional[Type[Response]] = ..., name: Optional[str] = ...) -> None:
        ...

    def api_route(self, path: str, *, response_model: Optional[Type[Any]] = ..., status_code: int = ..., tags: Optional[List[str]] = ..., dependencies: Optional[Sequence[Depends]] = ..., summary: Optional[str] = ..., description: Optional[str] = ..., response_description: str = ..., responses: Optional[Dict[Union[int, str], Dict[str, Any]]] = ..., deprecated: Optional[bool] = ..., methods: Optional[List[str]] = ..., operation_id: Optional[str] = ..., response_model_include: Optional[Union[SetIntStr, DictIntStrAny]] = ..., response_model_exclude: Optional[Union[SetIntStr, DictIntStrAny]] = ..., response_model_by_alias: bool = ..., response_model_exclude_unset: bool = ..., response_model_exclude_defaults: bool = ..., response_model_exclude_none: bool = ..., include_in_schema: bool = ..., response_class: Optional[Type[Response]] = ..., name: Optional[str] = ...) -> Callable:
        ...

    def add_api_websocket_route(self, path: str, endpoint: Callable, name: Optional[str] = ...) -> None:
        ...

    def websocket(self, path: str, name: Optional[str] = ...) -> Callable:
        ...

    def include_router(self, router: routing.APIRouter, *, prefix: str = ..., tags: Optional[List[str]] = ..., dependencies: Optional[Sequence[Depends]] = ..., responses: Optional[Dict[Union[int, str], Dict[str, Any]]] = ..., default_response_class: Optional[Type[Response]] = ...) -> None:
        ...

    def get(self, path: str, *, response_model: Optional[Type[Any]] = ..., status_code: int = ..., tags: Optional[List[str]] = ..., dependencies: Optional[Sequence[Depends]] = ..., summary: Optional[str] = ..., description: Optional[str] = ..., response_description: str = ..., responses: Optional[Dict[Union[int, str], Dict[str, Any]]] = ..., deprecated: Optional[bool] = ..., operation_id: Optional[str] = ..., response_model_include: Optional[Union[SetIntStr, DictIntStrAny]] = ..., response_model_exclude: Optional[Union[SetIntStr, DictIntStrAny]] = ..., response_model_by_alias: bool = ..., response_model_exclude_unset: bool = ..., response_model_exclude_defaults: bool = ..., response_model_exclude_none: bool = ..., include_in_schema: bool = ..., response_class: Optional[Type[Response]] = ..., name: Optional[str] = ..., callbacks: Optional[List[routing.APIRoute]] = ...) -> Callable:
        ...

    def put(self, path: str, *, response_model: Optional[Type[Any]] = ..., status_code: int = ..., tags: Optional[List[str]] = ..., dependencies: Optional[Sequence[Depends]] = ..., summary: Optional[str] = ..., description: Optional[str] = ..., response_description: str = ..., responses: Optional[Dict[Union[int, str], Dict[str, Any]]] = ..., deprecated: Optional[bool] = ..., operation_id: Optional[str] = ..., response_model_include: Optional[Union[SetIntStr, DictIntStrAny]] = ..., response_model_exclude: Optional[Union[SetIntStr, DictIntStrAny]] = ..., response_model_by_alias: bool = ..., response_model_exclude_unset: bool = ..., response_model_exclude_defaults: bool = ..., response_model_exclude_none: bool = ..., include_in_schema: bool = ..., response_class: Optional[Type[Response]] = ..., name: Optional[str] = ..., callbacks: Optional[List[routing.APIRoute]] = ...) -> Callable:
        ...

    def post(self, path: str, *, response_model: Optional[Type[Any]] = ..., status_code: int = ..., tags: Optional[List[str]] = ..., dependencies: Optional[Sequence[Depends]] = ..., summary: Optional[str] = ..., description: Optional[str] = ..., response_description: str = ..., responses: Optional[Dict[Union[int, str], Dict[str, Any]]] = ..., deprecated: Optional[bool] = ..., operation_id: Optional[str] = ..., response_model_include: Optional[Union[SetIntStr, DictIntStrAny]] = ..., response_model_exclude: Optional[Union[SetIntStr, DictIntStrAny]] = ..., response_model_by_alias: bool = ..., response_model_exclude_unset: bool = ..., response_model_exclude_defaults: bool = ..., response_model_exclude_none: bool = ..., include_in_schema: bool = ..., response_class: Optional[Type[Response]] = ..., name: Optional[str] = ..., callbacks: Optional[List[routing.APIRoute]] = ...) -> Callable:
        ...

    def delete(self, path: str, *, response_model: Optional[Type[Any]] = ..., status_code: int = ..., tags: Optional[List[str]] = ..., dependencies: Optional[Sequence[Depends]] = ..., summary: Optional[str] = ..., description: Optional[str] = ..., response_description: str = ..., responses: Optional[Dict[Union[int, str], Dict[str, Any]]] = ..., deprecated: Optional[bool] = ..., operation_id: Optional[str] = ..., response_model_include: Optional[Union[SetIntStr, DictIntStrAny]] = ..., response_model_exclude: Optional[Union[SetIntStr, DictIntStrAny]] = ..., response_model_by_alias: bool = ..., response_model_exclude_unset: bool = ..., response_model_exclude_defaults: bool = ..., response_model_exclude_none: bool = ..., include_in_schema: bool = ..., response_class: Optional[Type[Response]] = ..., name: Optional[str] = ..., callbacks: Optional[List[routing.APIRoute]] = ...) -> Callable:
        ...

    def options(self, path: str, *, response_model: Optional[Type[Any]] = ..., status_code: int = ..., tags: Optional[List[str]] = ..., dependencies: Optional[Sequence[Depends]] = ..., summary: Optional[str] = ..., description: Optional[str] = ..., response_description: str = ..., responses: Optional[Dict[Union[int, str], Dict[str, Any]]] = ..., deprecated: Optional[bool] = ..., operation_id: Optional[str] = ..., response_model_include: Optional[Union[SetIntStr, DictIntStrAny]] = ..., response_model_exclude: Optional[Union[SetIntStr, DictIntStrAny]] = ..., response_model_by_alias: bool = ..., response_model_exclude_unset: bool = ..., response_model_exclude_defaults: bool = ..., response_model_exclude_none: bool = ..., include_in_schema: bool = ..., response_class: Optional[Type[Response]] = ..., name: Optional[str] = ..., callbacks: Optional[List[routing.APIRoute]] = ...) -> Callable:
        ...

    def head(self, path: str, *, response_model: Optional[Type[Any]] = ..., status_code: int = ..., tags: Optional[List[str]] = ..., dependencies: Optional[Sequence[Depends]] = ..., summary: Optional[str] = ..., description: Optional[str] = ..., response_description: str = ..., responses: Optional[Dict[Union[int, str], Dict[str, Any]]] = ..., deprecated: Optional[bool] = ..., operation_id: Optional[str] = ..., response_model_include: Optional[Union[SetIntStr, DictIntStrAny]] = ..., response_model_exclude: Optional[Union[SetIntStr, DictIntStrAny]] = ..., response_model_by_alias: bool = ..., response_model_exclude_unset: bool = ..., response_model_exclude_defaults: bool = ..., response_model_exclude_none: bool = ..., include_in_schema: bool = ..., response_class: Optional[Type[Response]] = ..., name: Optional[str] = ..., callbacks: Optional[List[routing.APIRoute]] = ...) -> Callable:
        ...

    def patch(self, path: str, *, response_model: Optional[Type[Any]] = ..., status_code: int = ..., tags: Optional[List[str]] = ..., dependencies: Optional[Sequence[Depends]] = ..., summary: Optional[str] = ..., description: Optional[str] = ..., response_description: str = ..., responses: Optional[Dict[Union[int, str], Dict[str, Any]]] = ..., deprecated: Optional[bool] = ..., operation_id: Optional[str] = ..., response_model_include: Optional[Union[SetIntStr, DictIntStrAny]] = ..., response_model_exclude: Optional[Union[SetIntStr, DictIntStrAny]] = ..., response_model_by_alias: bool = ..., response_model_exclude_unset: bool = ..., response_model_exclude_defaults: bool = ..., response_model_exclude_none: bool = ..., include_in_schema: bool = ..., response_class: Optional[Type[Response]] = ..., name: Optional[str] = ..., callbacks: Optional[List[routing.APIRoute]] = ...) -> Callable:
        ...

    def trace(self, path: str, *, response_model: Optional[Type[Any]] = ..., status_code: int = ..., tags: Optional[List[str]] = ..., dependencies: Optional[Sequence[Depends]] = ..., summary: Optional[str] = ..., description: Optional[str] = ..., response_description: str = ..., responses: Optional[Dict[Union[int, str], Dict[str, Any]]] = ..., deprecated: Optional[bool] = ..., operation_id: Optional[str] = ..., response_model_include: Optional[Union[SetIntStr, DictIntStrAny]] = ..., response_model_exclude: Optional[Union[SetIntStr, DictIntStrAny]] = ..., response_model_by_alias: bool = ..., response_model_exclude_unset: bool = ..., response_model_exclude_defaults: bool = ..., response_model_exclude_none: bool = ..., include_in_schema: bool = ..., response_class: Optional[Type[Response]] = ..., name: Optional[str] = ..., callbacks: Optional[List[routing.APIRoute]] = ...) -> Callable:
        ...
