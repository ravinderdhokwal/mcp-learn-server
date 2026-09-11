import json

from pydantic import ValidationError

from mcp_learn_server.jsonrpc.models import Request, Notification
from mcp_learn_server.jsonrpc.errors import JSONRPCError, ErrorCode


def parse_message(raw: bytes | str) -> Request | Notification:
    try:
        data = json.loads(raw)
    except json.JSONDecodeError as exc:
        raise JSONRPCError(
            ErrorCode.PARSE_ERROR,
            "Invalid JSON was received by the server.",
            data={"parse_error": str(exc)}
        ) from exc

    if not isinstance(data, dict):
        raise JSONRPCError(
            ErrorCode.INVALID_REQUEST,
            f"Expected a JSON object, got {type(data).__name__}."
        )

    is_request = "id" in data

    try:
        if is_request:
            return Request.model_validate(data)
        else:
            return Notification.model_validate(data)
    except ValidationError as exc:
        raise JSONRPCError(
            ErrorCode.INVALID_REQUEST,
            f"Malformed {'request' if is_request else 'notification'}: {exc.error_count()} validation error(s).",
            data={"validation_errors": exc.errors()},
        ) from exc
        