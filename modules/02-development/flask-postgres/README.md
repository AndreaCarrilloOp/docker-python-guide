# Module 02 — Development · Flask

[Learning path](../../../README.md) · [Previous lesson](../../../modules/01-containerization/flask-basic/README.md) · [Next lesson →](../../../modules/03-linting-typing/FLASK.md)

## What you'll learn

Connect the application to PostgreSQL and verify persistence and service networking.

## Prerequisites

Complete the previous lesson in this track. 

## What's new

Service-backed API, Compose configuration and named volumes.

## Step 1 — Extend the basic application

The [source](app.py) adds a SQLAlchemy Task model, an application factory and CRUD endpoints. The database connection is created from environment variables; create_all initializes the teaching schema. Review [requirements.txt](requirements.txt) and the reused Dockerfile.

## Step 2 — Connect services

Read [compose.yaml](compose.yaml). Compose builds the app, starts PostgreSQL, provides DNS by service name (db), waits for the dependency health check and persists data with a named volume. Only the API binds to a host port. POSTGRES_PASSWORD is supplied in an ignored local .env file.

## Step 3 — Run

```bash
cd modules/02-development/flask-postgres
cp .env.example .env
# PowerShell: Copy-Item .env.example .env
# Edit .env with a unique local POSTGRES_PASSWORD
docker compose up --build -d --wait
docker compose ps
```

## Step 4 — Try the API

```bash
curl -f http://localhost:5000/health
curl -X POST http://localhost:5000/tasks -H 'Content-Type: application/json' -d '{"title":"Learn Docker"}'
curl http://localhost:5000/tasks
```

Expected: health status healthy, HTTP 201 for creation and JSON list containing the new record. Use its returned id to GET and DELETE it. PUT /tasks/{id} updates a task.

## Optional — Inspect service data

```bash
docker compose --profile tools up -d
```
Open http://localhost:8080. Adminer: select PostgreSQL, server db, user and database from .env, and your local password.

Stop with docker compose --profile tools down. Add -v only to intentionally delete lab data.

## Troubleshooting

Use docker compose logs and docker compose ps to inspect unhealthy services. Ensure the API connects to the service name rather than localhost.

## Key takeaway

Compose connects independently managed services.

[Learning path](../../../README.md) · [Previous lesson](../../../modules/01-containerization/flask-basic/README.md) · [Next lesson →](../../../modules/03-linting-typing/FLASK.md)
