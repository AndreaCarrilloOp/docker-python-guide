# Module 03 — Code Quality

[Previous module](../02-development/README.md) · [Next module](../04-cicd/README.md)

## Overview

Add linting, type checking and functional tests.

Complete the preceding checkpoint first.

## Learning objectives

- Add linting, type checking and functional tests.
- Understand the relationship between Python application code and its runtime configuration.
- Verify a working example before continuing.

## Examples

| Track | Example |
|---|---|
| Flask | [flask-quality](flask-quality/README.md) |
| FastAPI | [fastapi-quality](fastapi-quality/README.md) |

## Implementation

From either example directory, create and activate a Python virtual environment, then run:

```bash
python -m pip install -r requirements.txt -r requirements-dev.txt
python -m ruff check .
python -m ruff format .
python -m pyright
python -m pytest tests -q
```

Ruff formats and checks syntax/imports; Pyright validates types with basic mode. The root pre-commit hooks are optional and require the quality tools installed in the active environment; run `pre-commit install` from the repository root.

## Validation

Follow the selected example README. Confirm that its functional tests pass and that the HTTP health endpoint responds successfully before moving on.

## Next checkpoint

[Next module](../04-cicd/README.md)
