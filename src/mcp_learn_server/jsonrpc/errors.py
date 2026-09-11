from enum import IntEnum
from typing import Any

class ErrorCode(IntEnum):
    PARSE_ERROR = -32700 # invalid JSON body
    INVALID_REQUEST = -32600 # valid JSON, but not a valid Request/Notification shape
    METHOD_NOT_FOUND = -32601 # method provided in the request doesn't exist / isn't available on the server
    INVALID_PARAMS = -32602 # params don't match what the method expects
    INTERNAL_ERROR = -32603 # anything unexpected on the server side

class JSONRPCError(Exception):
    def __init__(self, code: ErrorCode, message: str, data: Any | None = None) -> None:
        self.code = code
        self.message = message
        self.data = data
        super().__init__(F"[{code.name} {message}]")
