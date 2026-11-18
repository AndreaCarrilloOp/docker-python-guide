# Module 04 — CI/CD with GitHub Actions · Flask

[Learning path](../../README.md) · [Previous lesson](../../modules/03-linting-typing/FLASK.md) · [Next lesson →](../../modules/05-deployment/FLASK.md)

## What you'll learn

Test and automate the containerized API without duplicating code.

## Prerequisites

Complete the previous lesson in this track. 

## What's new

HTTP lifecycle tests and the repository-level workflow.

## Step 1 — Start the existing API

```bash
cd modules/02-development/flask-postgres
# Ensure .env contains a local password.
docker compose up --build -d --wait
```

## Step 2 — Test real HTTP requests

The tests in the [tests directory](../../modules/02-development/flask-postgres/tests) use Python's standard HTTP client and Pytest against the running API. They verify status codes and the task CRUD lifecycle; no simulated database is required.

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt -r ../../../requirements-dev.txt
python -m pytest tests -q
```

Expected: health and lifecycle tests pass. Clean up with docker compose down.

## Step 3 — Automate the workflow

Read [ci.yml](../../.github/workflows/ci.yml). A matrix selects each existing example. On push or pull request, the runner installs dependencies, runs Ruff and Pyright, builds the image, starts services, checks HTTP, runs Pytest and cleans up. Kubernetes manifest checks run separately.

Open the repository Actions tab and review the job for Flask. A successful workflow demonstrates integration and build verification; deployment is the next lesson, not an automatic cloud release.

## Troubleshooting

If tests cannot connect, verify the health endpoint first. Review the failed Actions step and container logs.

## Key takeaway

CI repeats the same checks automatically.

[Learning path](../../README.md) · [Previous lesson](../../modules/03-linting-typing/FLASK.md) · [Next lesson →](../../modules/05-deployment/FLASK.md)
