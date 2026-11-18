# fastapi-app

[Module guide](../README.md)

A user API backed by Redis, with expiring cache records. This checkpoint retains the development API.

## Run

From the repository root, enter this directory:

```bash
cd modules/04-cicd/fastapi-app
```

```bash
docker compose up --build -d --wait
docker compose ps
```

Stop services with `docker compose down`. Add `-v` only when deliberately deleting lab data.

## Verify

Open http://localhost:8000/health. Interactive API documentation: http://localhost:8000/docs.

Example resource: http://localhost:8000/users.

## Tests

Use a fresh Python 3.11 virtual environment in this directory. On Bash, run `python -m venv .venv` and `source .venv/bin/activate`; on PowerShell, run `python -m venv .venv` and `.\.venv\Scripts\Activate.ps1`.

```bash
python -m pip install -r requirements.txt -r requirements-dev.txt
python -m pytest tests -q
```

For code quality, run `python -m ruff check .` and `python -m pyright`.

Continue to the next checkpoint in the module navigation.
