from http import HTTPStatus
from typing import Literal
import json

def build_response(http_status: Literal[HTTPStatus.OK], body: dict):
    return {
        "statusCode": http_status,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps(body),
    }
