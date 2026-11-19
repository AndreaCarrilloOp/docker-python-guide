# 04 · CI/CD with GitHub Actions

[← FastAPI track](../../tracks/FASTAPI.md) · 4/5

Automate functional tests and container verification for the same application.

## 1. Run the API and tests

```bash
cd modules/02-development/fastapi-redis
docker compose up --build -d --wait
```

Activate the [environment from module 03](../../docs/lab-setup.md#python-environment).

Read the HTTP tests. They exercise the live API and Redis, not a simulated database.

```bash
python -m pytest tests -q
```

Expected: health and user lifecycle tests pass.

## 2. Understand the pipeline

Open `ci.yml`. The matrix runs each example separately on GitHub Actions.

```text
Install → Lint & type check → Build & run → HTTP tests → Cleanup
```

Review the job for FastAPI in [Actions](https://github.com/AndreaCarrilloOp/docker-python-guide/actions). CI validates the build; it does not publish to a cloud environment.

Stop Compose using [cleanup instructions](../../docs/lab-setup.md#compose).

## Solution

[`test_main.py`](../02-development/fastapi-redis/tests/test_main.py) · [`ci.yml`](../../.github/workflows/ci.yml)

---

[← Linting and typing](../03-linting-typing/FASTAPI.md) · [Test your deployment →](../05-deployment/FASTAPI.md)
