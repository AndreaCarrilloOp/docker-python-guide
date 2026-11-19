# 02 · Development

**FastAPI track · Module 02/05** · ●●○○○

[All modules](../../tracks/FASTAPI.md) · [Solution ↓](#solution)

Extend the basic application with Redis using Docker Compose.

## 1. Extend the application

Review [main.py](fastapi-redis/main.py) and [requirements.txt](fastapi-redis/requirements.txt).

Pydantic defines user request/response models. Redis stores records under user:* keys, assigns incrementing IDs and expires records after one hour. Synchronous routes run in FastAPI's worker threads.

## 2. Connect the services

Read [compose.yaml](fastapi-redis/compose.yaml). The API uses internal DNS (`redis`), waits for the dependency health check and uses a named volume for data.

```bash
cd modules/02-development/fastapi-redis
```
```bash
docker compose up --build -d --wait
docker compose ps
```

## 3. Verify the API

```bash
curl -f http://localhost:8000/health
curl -X POST http://localhost:8000/users -H 'Content-Type: application/json' -d '{"name":"Demo","email":"demo@example.com"}'
curl http://localhost:8000/users
```

Expected: HTTP 200 for health, 201 for creation and a JSON list containing the new record. Use its returned ID to retrieve or delete it. Explore other routes at http://localhost:8000/docs.

<details>
<summary>Optional · Redis Commander</summary>

```bash
docker compose --profile tools up -d
```

Open http://localhost:8081. Inspect keys using the configured Redis connection.

</details>

Stop the lab following [Compose cleanup](../../docs/lab-setup.md#compose) before continuing.

## Solution

Complete service-backed application, extended from module 01.

[Project files](fastapi-redis/) · [main.py](fastapi-redis/main.py) · [Compose](fastapi-redis/compose.yaml) · [Dockerfile](fastapi-redis/Dockerfile) · [Requirements](fastapi-redis/requirements.txt)

[.dockerignore](fastapi-redis/.dockerignore)

---

[← Module 01](../01-containerization/FASTAPI.md) · [All modules](../../tracks/FASTAPI.md) · [Module 03 →](../03-linting-typing/FASTAPI.md)
