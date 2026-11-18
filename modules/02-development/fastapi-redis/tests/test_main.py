from fastapi.testclient import TestClient
from fakeredis import FakeRedis
import main


def test_user_lifecycle(monkeypatch):
    monkeypatch.setattr(main, "cache", FakeRedis(decode_responses=True))
    client = TestClient(main.app)
    assert client.get("/health").status_code == 200
    assert client.post("/users", json={}).status_code == 422
    response = client.post("/users", json={"name": "Demo", "email": "demo@example.com"})
    assert response.status_code == 201
    user = response.json()
    path = f"/users/{user['id']}"
    assert client.get(path).json() == user
    assert client.get("/users").json() == [user]
    assert client.delete(path).status_code == 204
    assert client.get(path).status_code == 404
    monkeypatch.setenv("ENVIRONMENT", "production")
    assert client.delete("/cache/flush").status_code == 403
