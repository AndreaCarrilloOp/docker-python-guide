# 02 · Development

**Flask track**

Extend the basic application with PostgreSQL using Docker Compose.

## 1. Extend the application

Review [app.py](flask-postgres/app.py) and [requirements.txt](flask-postgres/requirements.txt).

The application factory configures SQLAlchemy, defines a Task model and exposes CRUD routes. The schema is initialized with create_all; connection settings come from environment variables.

## 2. Connect the services

Read [compose.yaml](flask-postgres/compose.yaml). The API uses internal DNS (`db`), waits for the dependency health check and uses a named volume for data.

```bash
cd modules/02-development/flask-postgres
cp .env.example .env
```
Edit `.env` and set a unique local `POSTGRES_PASSWORD`. In PowerShell, copy with `Copy-Item .env.example .env`. Never commit the file.

```bash
docker compose up --build -d --wait
docker compose ps
```

## 3. Verify the API

```bash
curl -f http://localhost:5000/health
curl -X POST http://localhost:5000/tasks -H 'Content-Type: application/json' -d '{"title":"Learn Docker"}'
curl http://localhost:5000/tasks
```

Expected: HTTP 200 for health, 201 for creation and a JSON list containing the new record. Use its returned ID to retrieve or delete it. Try PUT /tasks/{id} to update it. The optional [seed SQL](flask-postgres/init.sql) applies after schema creation.

<details>
<summary>Optional · Adminer</summary>

```bash
docker compose --profile tools up -d
```

Open http://localhost:8080. Choose PostgreSQL and use server db, database, username and password from your local .env.

</details>

Stop the lab following [Compose cleanup](../../docs/lab-setup.md#compose) before continuing.

---

[Course home](../../README.md) · [← Module 01](../01-containerization/FLASK.md) · [Module 03 →](../03-linting-typing/FLASK.md)
