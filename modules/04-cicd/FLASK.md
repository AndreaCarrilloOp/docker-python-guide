# 04 · CI/CD with GitHub Actions

[← Flask track](../../tracks/FLASK.md) · 4/5

Automate functional tests and container verification for the same application.

## 1. Run the API and tests

```bash
cd modules/02-development/flask-postgres
docker compose up --build -d --wait
```

Reuse your local .env from module 02. Activate the [environment from module 03](../../docs/lab-setup.md#python-environment).

Read the HTTP tests. They exercise the live API and PostgreSQL, not a simulated database.

```bash
python -m pytest tests -q
```

Expected: health and task CRUD tests pass.

## 2. Understand the pipeline

Open `ci.yml`. The matrix runs each example separately on GitHub Actions.

```text
Install → Lint & type check → Build & run → HTTP tests → Cleanup
```

Review the job for Flask in [Actions](https://github.com/AndreaCarrilloOp/docker-python-guide/actions). CI validates the build; it does not publish to a cloud environment.

Stop Compose using [cleanup instructions](../../docs/lab-setup.md#compose).

## Solution

[`test_app.py`](../02-development/flask-postgres/tests/test_app.py) · [`ci.yml`](../../.github/workflows/ci.yml)

---

[← Linting and typing](../03-linting-typing/FLASK.md) · [Test your deployment →](../05-deployment/FLASK.md)
