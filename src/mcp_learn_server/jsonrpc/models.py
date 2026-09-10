from typing import Any, Literal
from pydantic import BaseModel, ConfigDict


JsonRpcVersionType = Literal["2.0"]
ParamsType = dict[str, Any] | list[Any] | None
IdType = str | int


JSONRPC_VERSON: JsonRpcVersionType = "2.0"

class Request(BaseModel):
    model_config = ConfigDict(extra="forbid")

    jsonrpc: JsonRpcVersionType
    id: IdType
    method: str
    params: ParamsType = None

class Notification(BaseModel):
    model_config = ConfigDict(extra="forbid")

    jsonrpc: JsonRpcVersionType
    method: str
    params: ParamsType = None

class ErrorObject(BaseModel):
    code: int
    message: str
    data: Any | None = None

class SuccessResponse(BaseModel):
    model_config = ConfigDict(extra="forbid")

    jsonrpc: JsonRpcVersionType = JSONRPC_VERSON
    id: IdType | None
    result = Any

class ErrorResponse(BaseModel):
    model_config = ConfigDict(extra="forbid")

    jsonrpc: JsonRpcVersionType = JSONRPC_VERSON
    id: IdType | None
    error: ErrorObject

Response = SuccessResponse | ErrorResponse