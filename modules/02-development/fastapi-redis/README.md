# Module 02 — Development · FastAPI

[Learning path](../../../README.md) · [Previous lesson](../../../modules/01-containerization/fastapi-basic/README.md) · [Next lesson →](../../../modules/03-linting-typing/FASTAPI.md)

## What you'll learn

Connect the application to Redis and verify persistence and service networking.

## Prerequisites

Complete the previous lesson in this track. 

## What's new

Service-backed API, Compose configuration and named volumes.

## Step 1 — Extend the basic application

The [source](main.py) adds Pydantic user models, Redis key storage, an incrementing ID, expiration and user endpoints. Redis calls are synchronous and FastAPI runs normal def routes in worker threads. Review [requirements.txt](requirements.txt) and the reused Dockerfile.

## Step 2 — Connect services

Read [compose.yaml](compose.yaml). Compose builds the app, starts Redis, provides DNS by service name (redis), waits for the dependency health check and persists data with a named volume. Only the API binds to a host port. REDIS_URL points to the internal redis service.

## Step 3 — Run

```bash
cd modules/02-development/fastapi-redis
docker compose up --build -d --wait
docker compose ps
```

## Step 4 — Try the API

```bash
curl -f http://localhost:8000/health
curl -X POST http://localhost:8000/users -H 'Content-Type: application/json' -d '{"name":"Demo","email":"demo@example.com"}'
curl http://localhost:8000/users
```

Expected: health status healthy, HTTP 201 for creation and JSON list containing the new record. Use its returned id to GET and DELETE it. /docs exposes the API interactively. Records expire after one hour.

## Optional — Inspect service data

```bash
docker compose --profile tools up -d
```
Open http://localhost:8081. Redis Commander: inspect keys in the redis service.

Stop with docker compose --profile tools down. Add -v only to intentionally delete lab data.

## Troubleshooting

Use docker compose logs and docker compose ps to inspect unhealthy services. Ensure the API connects to the service name rather than localhost.

## Key takeaway

Compose connects independently managed services.

[Learning path](../../../README.md) · [Previous lesson](../../../modules/01-containerization/fastapi-basic/README.md) · [Next lesson →](../../../modules/03-linting-typing/FASTAPI.md)
