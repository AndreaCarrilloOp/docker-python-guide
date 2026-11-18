from fastapi.testclient import TestClient
from main import app


def test_root_and_health():
    client = TestClient(app)
    assert client.get("/").status_code == 200
    assert client.get("/health").json()["status"] == "healthy"
