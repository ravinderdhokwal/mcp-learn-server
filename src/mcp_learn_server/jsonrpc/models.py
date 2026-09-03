from typing import Any, Union, Literal
from pydantic import BaseModel, ConfigDict


JSONRPC_VERSON = "2.0"

ParamsType = dict[str, Any] | list[Any] | None

IdType = Union[str, int]


class Request(BaseModel):
    model_config = ConfigDict(extra="forbid")

    jsonrpc: Literal["2.0"]
    id: IdType
    method: str
    params: ParamsType = None

class Notification(BaseModel):
    model_config = ConfigDict(extra="forbid")

    jsonrpc: Literal["2.0"]
    method: str
    params: ParamsType = None

class ErrorObject(BaseModel):
    code: int
    message: str
    data: Any | None = None

class SuccessResponse(BaseModel):
    model_config = ConfigDict(extra="forbid")

    jsonrpc: Literal["2.0"] = JSONRPC_VERSON
    id: IdType | None
    result = Any

class ErrorResponse(BaseModel):
    model_config = ConfigDict(extra="forbid")

    jsonrpc: Literal["2.0"] = JSONRPC_VERSON
    id: IdType | None
    error: ErrorObject

Response = Union[SuccessResponse, ErrorResponse]