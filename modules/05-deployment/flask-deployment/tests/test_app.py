from app import create_app


def test_task_lifecycle():
    client = create_app("sqlite:///:memory:").test_client()
    assert client.get("/health").status_code == 200
    assert client.post("/tasks", json={}).status_code == 400
    response = client.post("/tasks", json={"title": "Learn Docker"})
    assert response.status_code == 201
    task = response.get_json()
    path = f"/tasks/{task['id']}"
    assert client.get(path).status_code == 200
    assert client.put(path, json={"completed": True}).get_json()["completed"] is True
    assert len(client.get("/tasks").get_json()) == 1
    assert client.delete(path).status_code == 204
    assert client.get(path).status_code == 404
