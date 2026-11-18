# Module 03 — Linting and typing · FastAPI

[Learning path](../../README.md) · [Previous lesson](../../modules/02-development/fastapi-redis/README.md) · [Next lesson →](../../modules/04-cicd/FASTAPI.md)

## What you'll learn

Use linting, formatting, static typing and pre-commit on existing source.

## Prerequisites

Complete the previous lesson in this track. 

## What's new

Shared quality configuration and development requirements.

## Step 1 — Prepare your existing example

Use the reference source from [module 02](../../modules/02-development/fastapi-redis/README.md); no new application is needed. Create a virtual environment in that example directory.

```bash
cd modules/02-development/fastapi-redis
python -m venv .venv
source .venv/bin/activate
# PowerShell: .\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt -r ../../../requirements-dev.txt
```

## Step 2 — Lint and format

Read the shared [pyproject.toml](../../pyproject.toml). Ruff detects import ordering, syntax and broad exception issues. Format explicitly, then run checks.

```bash
python -m ruff check .
python -m ruff check --fix .
python -m ruff format .
python -m ruff check .
```

## Step 3 — Type check

```bash
python -m pyright .
```

Inspect Pydantic request/response models and the isinstance checks that narrow Redis responses before JSON decoding or arithmetic.

## Step 4 — Automate local quality checks

With the environment active, return to the repository root and run:

```bash
cd ../../..
pre-commit install
pre-commit run --all-files
```

The shared [.pre-commit-config.yaml](../../.pre-commit-config.yaml) runs Ruff. Format any reported files and rerun. Expected: no lint or type errors and passing hooks. Do not suppress type errors to make a check pass.

## Troubleshooting

Check that your virtual environment is active. Resolve reported imports and type errors before committing.

## Key takeaway

Quality tools complement functional tests.

[Learning path](../../README.md) · [Previous lesson](../../modules/02-development/fastapi-redis/README.md) · [Next lesson →](../../modules/04-cicd/FASTAPI.md)
