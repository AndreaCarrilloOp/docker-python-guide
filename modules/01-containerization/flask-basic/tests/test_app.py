from app import app


def test_root_and_health():
    client = app.test_client()
    assert client.get("/").status_code == 200
    assert client.get("/health").get_json()["status"] == "healthy"
