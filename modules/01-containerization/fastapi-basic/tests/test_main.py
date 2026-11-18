"""HTTP tests against the running tutorial application."""
import json
import os
from urllib.error import HTTPError
from urllib.request import Request, urlopen

BASE_URL = os.getenv("GUIDE_BASE_URL", "http://127.0.0.1:8000")


def request(method: str, path: str, data: dict | None = None):
    payload = json.dumps(data).encode() if data is not None else None
    req = Request(
        BASE_URL + path, data=payload, method=method,
        headers={"Content-Type": "application/json"},
    )
    try:
        with urlopen(req, timeout=10) as response:
            body = response.read()
            return response.status, body
    except HTTPError as error:
        return error.code, error.read()


def test_health():
    status, body = request("GET", "/health")
    assert status == 200
    assert json.loads(body)["status"] == "healthy"


def test_root():
    status, body = request("GET", "/")
    assert status == 200
    assert "message" in json.loads(body)
