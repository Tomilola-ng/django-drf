""" Exception Handler """

from typing import Any, Optional
from http import HTTPStatus

from rest_framework.views import exception_handler
from rest_framework.response import Response

HTTP_CODE_TO_MESSAGE = {v.value: v.description for v in HTTPStatus}


def api_exception_handler(exc: Exception, context: dict[str, Any]) -> Optional[Response]:
    """
    Custom API Exception Handler

    Args:
        exc (Exception): The exception object
        context (dict): The exception context

    Returns:
        Optional[Response]: A Response object if an exception is handled, None otherwise
    """

    response = exception_handler(exc, context)

    if response is None:
        return None

    error_payload = {
        "error": {
            "status_code": response.status_code,
            "message": HTTP_CODE_TO_MESSAGE.get(response.status_code, str(exc)),
            "details": response.data
        }
    }

    response.data = error_payload

    return response
