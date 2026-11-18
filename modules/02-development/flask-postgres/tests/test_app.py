"""HTTP tests against the running tutorial application."""
import json
import os
from urllib.error import HTTPError
from urllib.request import Request, urlopen

BASE_URL = os.getenv("GUIDE_BASE_URL", "http://127.0.0.1:5000")


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


def test_task_lifecycle():
    assert request("POST", "/tasks", {})[0] == 400
    status, body = request("POST", "/tasks", {"title": "Learn Docker"})
    assert status == 201
    task = json.loads(body)
    path = f"/tasks/{task['id']}"
    try:
        assert request("GET", path)[0] == 200
        status, body = request("PUT", path, {"completed": True})
        assert status == 200
        assert json.loads(body)["completed"] is True
        assert request("PUT", path, {"completed": "yes"})[0] == 400
        status, body = request("GET", "/tasks")
        assert status == 200
        assert any(item["id"] == task["id"] for item in json.loads(body))
    finally:
        assert request("DELETE", path)[0] == 204
    assert request("GET", path)[0] == 404
